"""
WSGI applications can be linked together to run one after another.
This is a common practice referred to as middleware.
Middleware is commonly used to add modularized functionality to a WSGI application.
"""

# A reference implementation of the WSGI specification.
# Not commonly used in production environments.
from wsgiref.simple_server import make_server


# A basic WSGI application.
def app(environ, start_response):
    # Begin by sending the HTTP(S) client the response status and headers.
    start_response('200 OK', [('Content-Type', 'text/plain')])
    # Attempt to locate a key in the environ dictionary named 'GREETING'
    # If it doesn't exist the default value of 'Hello' is used.
    greeting = environ.get('GREETING', 'Hello')
    # The encode method is used to convert a str object into a bytestring.
    yield f'{greeting}, WSGI!\n'.encode()


class Middleware():
    ''' A callable class used to set a WSGI app when the class is initialized.
        The __call__ magic method makes the instantiated object callable.
    '''
    def __init__(self, wsgi_app):
        ''' Args:
                wsgi_app | The WSGI application to call after this middleware runs.
        '''
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        # Perform middleware functionality here.
        # This example adds a new key-value-pair to the environ dictionary.
        # Editing the dictionary allows middleware to pass data to the next
        # WSGI application.
        environ['GREETING'] = 'Hey'
        # Call the provided WSGI application passing it the revised environ dictionary.
        return self.wsgi_app(environ, start_response)


if __name__ == '__main__':
    # Create a server and run the app until the process is terminated.
    # The WSGI application (app) is passed to the constructor of the Middleware class.
    # The WSGI server will call the Middleware object which will run the __call__ method.
    server = make_server('', 5000, Middleware(app))
    server.serve_forever()

"""
Middleware is commonly used in WSGI applications to provide low level functionality. 
For example: serving static files, security related tasks, request redirection, etc. 
Middleware is essentially just another WSGI application. 
Python web application frameworks commonly chain multiple middleware applications together. 
Chaining middleware in a specific order enables the middleware to perform its given task and optionally call the next application in the chain.
"""