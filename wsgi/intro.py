"""
The Web Server Gateway Interface is a simple universal-interface between web servers and web applications. In 2003 there were many popular Python web application frameworks. At the time the interface between servers and applications was implementation specific. The lack of standards locked engineers into using specific web servers and or web frameworks.
The application-side callable is required to include two positional parameters. The WSGI server is responsible for calling the callable for each HTTP request made to the server.

The first argument is a dictionary which contains WSGI environment variables. The second is a callable used to write the HTTP response status and headers. The application is required to return an iterable which will become the HTTP response body.
A WSGI application is provided to a WSGI server during server creation. WSGI servers range in functionality, capabilities, and configuration options. The built-in reference implementation is relatively limited in functionality. However, production servers such as
gunicorn
, opens in a new tab and
uwsgi
, opens in a new tab are much more feature rich.
"""
# A reference implementation of the WSGI specification.
# Not commonly used in production environments.
from wsgiref.simple_server import make_server
# A basic WSGI application.
def app(environ, start_response):
    # Begin by sending the HTTP(S) client the response status and headers.
    # Web applications support a wide variety of content types such as html, images, plain text, etc.
    # Because the demonstrations in this lab are consumed using the console, plain text is used.
    start_response('200 OK', [('Content-Type', 'text/plain')])
    # Yield a bytestring representing the response body.
    # The yield keyword turns this function intro a generator
    # making the function an iterable.
    # The b in front of the open quote makes this a bytestring.
    yield b'Hello, WSGI!\n'

if __name__ == '__main__':
    # Create a server and run the app until the process is terminated.
    # The 1st argument to make_server is the hostname for which the server is bound.
    # The 2nd argument to make_server is the network port used to listen for requests.
    # The 3rd argument to make_server is the WSGI application callable.
    # Other arguments exist. See documentation for more details.
    server = make_server('', 5000, app)
    server.serve_forever()


