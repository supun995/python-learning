"""
Most Python web development doesn't occur at the WSGI level. WSGI is designed to move HTTP messages between clients and servers. It intentionally omits higher level functionality which is expected to be provided by a WSGI compliant web framework.

WSGI frameworks such as
Flask
, opens in a new tab,
Django
, opens in a new tab, and
CherryPy
, opens in a new tab, among others include the types of high level features expected in a modern web framework. Features such as: URL path routing, query string parsing, template rendering, etc.

The application created in this step highlights some of the features required to create a more functional web application
"""

from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

class Application():
    ''' A callable class serving as a WSGI application. '''

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
            # Store a tuple containing the handler callable and any optional arguments.
            self.path_handlers[path] = (handler, args, kwargs)
        return wrap


    def __call__(self, environ, start_response):
        response_headers = [('Content-Type', 'text/plain')]
        request_url_path = environ.get('PATH_INFO', '')

        # Attempt to locate the callable for the current path.
        # If missing this is a 404 -- file not found -- error.
        if request_url_path not in self.path_handlers:
            start_response('404 Not Found', response_headers)
            return [f'{request_url_path} not found!'.encode()]

        try:
            # Unpack the handler callable and arguments
            handler, args, kwargs = self.path_handlers[request_url_path]
            response_body = handler(*args, **kwargs)
            # Call start_response only if the handler returned without error.
            start_response('200 OK', response_headers)
            # Show the unparsed query string for comparison.
            query_str_orig = environ['QUERY_STRING']
            # Get the parsed query string or return an empty dictionary.
            query_str_dict = environ.get('QUERY_STRING_PARSED', {})
            # Build the multi-line query string display.
            query_str_display = [f'key: {key}, value: {value}' for key, value in query_str_dict.items()]
            query_str_display = '\n'.join(query_str_display)
            # Return both the response body, the original unparsed query string,
            # and the parsed query string values.
            return [
                response_body,
                f'The original query string: {query_str_orig}\n'.encode(),
                query_str_display.encode()
            ]
        except Exception as ex:
            # If the handler fails, display a 500 error.
            start_response('500 Internal Server Error', response_headers)
            return [str(ex).encode()]


"""
Modular WSGI applications can become middleware used to extend the functionality of a WSGI application. 
Self contained functionality such as parsing URL query strings is generalized enough to become middleware.

When the below QueryStringParser object is called it uses the parse_qs callable to parse the WSGI server-provided URL query string. The parse_qs callable returns a dictionary of key-value pairs from the query string. The environ argument is updated to store the parsed dictionary with the key QUERY_STRING_PARSED.
"""
class QueryStringParser():
    ''' A basic WSGI middleware example.

        This middleware parses the URL query string converting it into a dictionary.
        The dictionary is added to the environment variables which are passed to the
        next WSGI application.
    '''

    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        environ['QUERY_STRING_PARSED'] = parse_qs(environ['QUERY_STRING'])
        # Ensure the application is called.
        return self.wsgi_app(environ, start_response)

# Create an instance of the WSGI application so it can be used
# to decorate the response body functions.
app = Application()

# Register the index function to the default URL path.
# When this code is first read by the interpreter the route method
# is called with a path of / and the decorated index function becomes the
# callable used to generate the HTTP response body.
@app.route('/')
def index():
    return b'Welcome! :)\n'

# Register the error function to the /error path.
# This will raise an error when called to test the 500 error.
@app.route('/error')
def error():
    # The following code will raise a ZeroDivisionError
    # https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
    return 1 / 0


if __name__ == '__main__':
    server = make_server('', 5000, QueryStringParser(app))
    server.serve_forever()

"""
The QueryStringParser middleware parses the query string from environ and saves the parsed results as a dictionary. 
When the middleware runs first the parsed results will be available to the WSGI application. 
Wrapping the application with the middleware enables it to run first.
"""