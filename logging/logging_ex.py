"""
Python's standard library includes a logging module. The logging module provides a default structure for log events, allowing for customization. Log events include a log level which indicates the severity of the message (DEBUG, INFO, WARNING, ERROR, CRITICAL). These levels are ordered by severity (least to greatest).
curl "localhost:5000/reverse-it?text=welcome"
"""
import logging
import sys
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

###############################################################################
# Configure the logger to use a more informative and structured format.
logger = logging.getLogger()
logger.setLevel(logging.INFO) #logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO) #logger.setLevel(logging.DEBUG)

handler.setFormatter(logging.Formatter('%(asctime)s\t%(name)s\t%(levelname)s\t%(lineno)d\t%(funcName)s\t%(message)s'))
logger.addHandler(handler)
###############################################################################
# request is a global used to store WSGI environment variables which
# are accessible to route handlers.
request = {}


class Application():
    def __init__(self):
        # A dictionary mapping path names to the function used to render the response body.
        self.path_handlers = {}

    def route(self, path):
        ''' A callable decorator used to register a path handler.

            Args:
                path | The path to register for the decorated callable.
        '''

        def wrap(handler, *args, **kwargs):
            ''' Args:
                    handler     | The callable to call when a request matches the path
                                  provided to the route method.

                                  The handler function isn't passed to the route method directly.
                                  When the route method is used as a decorator the decorated callable
                                  is passed to this wrap function.
                    args        | Optional positional arguments to pass to the handler when called.
                    kwargs      | Optional keyword arguments to pass to the handler when called.

            '''
            logging.info(f'registering route for path: {path}')
            # Store a tuple containing the handler callable and any optional arguments.
            self.path_handlers[path] = (handler, args, kwargs)

        return wrap

    def __call__(self, environ, start_response):
        response_headers = [('Content-Type', 'text/plain')]
        request_url_path = environ.get('PATH_INFO', '')

        logging.info(f'request made for path: {request_url_path}')

        # Attempt to locate the callable for the current path.
        # If missing this is a 404 -- file not found -- error.
        if request_url_path not in self.path_handlers:
            logging.info(f'(404) path not found: {request_url_path}')
            start_response('404 Not Found', response_headers)
            return [f'{request_url_path} not found!'.encode()]

        try:
            # Unpack the handler callable and arguments
            handler, args, kwargs = self.path_handlers[request_url_path]
            # Set the global request binding to the environ
            global request
            request = environ
            # The route handler is now able to access the environment variables.
            response_body = handler(*args, **kwargs)
            # Call start_response only if the handler returned without error.
            start_response('200 OK', response_headers)
            # Log the success up until this point.
            logging.info('(200) response header sent')
            # Also log the response body as a debugging option.
            logging.debug(f'response body: {response_body}')
            # WSGI requires the response body to be iterable.
            return [response_body, b'\n']
        except Exception as ex:
            logging.exception(f'(500) failed running handler for path: {request_url_path}')
            # If the handler failed display a 500 error.
            start_response('500 Internal Server Error', response_headers)
            return [str(ex).encode(), b'\n']


class QueryStringParser():
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        query_string = environ['QUERY_STRING']

        logging.debug(f'query string (before) : {query_string}')
        # Add the parsed query string to the environ dictionary.
        # The key QUERY_STRING_PARSED will be available to
        # applications called after this middleware.
        environ['QUERY_STRING_PARSED'] = query_string = parse_qs(query_string)
        # Ensure the application is called.
        logging.debug(f'query string (after) : {query_string}')
        # Call the next app and pass the modified environment variables.
        return self.wsgi_app(environ, start_response)


# Create an instance of the WSGI application so it can be used
# to decorate the response body functions.
app = Application()


# Register the index function to the default path.
@app.route('/')
def index():
    return b'Welcome! :)'


@app.route('/reverse-it')
def reverse_it():
    return request['QUERY_STRING_PARSED'].get('text', '')[::-1].encode() #return request['QUERY_STRING_PARSED'].get('text', [])[0][::-1].encode()


if __name__ == '__main__':
    server = make_server('', 5000, QueryStringParser(app))
    server.serve_forever()
