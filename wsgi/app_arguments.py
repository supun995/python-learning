"""

Understanding WSGI applications requires an understanding of the application structure. WSGI applications are designed to respond to HTTP requests. HTTP is based on the idea of sending messages between a client and server. Clients send request messages to servers and servers send back response messages.

WSGI applications are called when a WSGI server receives an HTTP request message. The server calls the application-callable and provides the required arguments.

The first argument is a dictionary object containing request details, environment and WSGI related data, and any other data the WSGI server may provide. The second argument is a callable used to set the HTTP response status and headers.

The callable is required to return an iterable of bytestrings. Iterables include any object which implements the __iter__ magic method. The return data becomes the body of the HTTP response message.
"""

# A reference implementation of the WSGI specification.
# Not commonly used in production environments.
from wsgiref.simple_server import make_server
# A basic WSGI application.
def app(environ, start_response):
    # Begin by sending the HTTP(S) client the response status and headers.
    # Web applications support a wide variety of content types such as html, images, plain text, etc.
    # Because the demonstrations in this lab are consumed using the console, plain text is used.
    start_response('500 Server error', [('Content-Type', 'text/plain'), ('Host', 'cloudacademy.com')])
    # Yield a bytestring representing the response body.
    # The yield keyword turns this function intro a generator
    # making the function an iterable.
    # The b in front of the open quote makes this a bytestring.
    yield b'Hello, WSGI!\n'

    # Create a visual separator.
    yield b'-' * 80
    # Display the data from the environ argument
    for key, value in environ.items():
        yield f'\n{key:<50} {value}'.encode()

if __name__ == '__main__':
    # Create a server and run the app until the process is terminated.
    # The 1st argument to make_server is the hostname for which the server is bound.
    # The 2nd argument to make_server is the network port used to listen for requests.
    # The 3rd argument to make_server is the WSGI application callable.
    # Other arguments exist. See documentation for more details.
    server = make_server('', 5000, app)
    server.serve_forever()
