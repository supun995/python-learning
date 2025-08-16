import os
import unittest
from pathlib import Path
from  playground import wsgi
# Disable playground.__init__.fix_lab_path which is used to fix the lab environment URL paths.
# Only required to run the flask app over HTTP at: /app
os.environ['APP_UNDER_TEST'] = '1'
# test image paths
IMAGE_FILE = Path(__file__).parent / 'images' / 'python_logo.png'
# Configure the file upload directory to isolate it from dev.
wsgi.app.config.update({'FILE_UPLOAD_FOLDER': Path(__file__).parent / 'images' / 'uploads'})

"""
Commonly applications built on top of frameworks require framework specific testing mechanisms. 
Web applications require HTTP clients to send requests and receive responses. 
Flask includes a test client with methods matching HTTP verbs: 
get post put etc. 
These methods return an instance of a 
TestResponse, which is an enhanced implementation of a standard flask response.

Flask's test client is created by calling the test_client method of an instance of the 
Flask
, opens in a new tab class.

The login route is responsible for providing users with a means of authenticating. POST requests sent to the login route check the request body for form fields named username and password. If the credentials are valid a key-value pair is added to flask's 
session
, opens in a new tab object. If the credentials are invalid an HTML page is returned with a message indicating the login failure.
"""
class WSGI:
    ''' A namespace for a test case base class that prevents WSGIBase from being run
        solo in addition to being a base class.
    '''
    class WSGIBase(unittest.TestCase):
        def setUp(self):
            # credentials in multiple formats.
            self.correct_creds = 'admin magic'.split()
            self.invalid_creds = 'X X'.split()
            # Convert into a dict to pass to the client's data kwarg.
            # Denormalized data is often useful in tests. Having access to the same data
            # in different formats can make tests easier to read / write tests.
            #
            # DRY code and or maximally efficient code isn't required for most testing.
            # Tests will be read more than written. Focus on readability.
            self.correct_creds_dict = dict(zip('username password'.split(), self.correct_creds))
            self.invalid_creds_dict = dict(zip('username password'.split(), self.invalid_creds))
            # routes.
            self.index = '/'
            self.image = '/image/'
            self.login = '/login'
            self.logout = '/logout'

class LoginIntegration(WSGI.WSGIBase):

    def test_login_valid(self):
        ''' allows valid user logins '''
        ###############################################################################
        #
        # Test Requirements (valid logins):
        #
        # Ensure valid users are able to log into the app.
        #
        # 1.) Send a POST request to the login route (self.login).
        #     - Include valid credentials (self.correct_creds_dict) in the request body.
        # 2.) Ensure the route handler adds a username key to the session object
        #     with the posted username as the value.
        # 3.) Ensure the response redirects to the image route (self.image).
        ###############################################################################
        with wsgi.app.test_client() as client:
            # Authenticate the default admin user.
            assert client.post(
                self.login,
                data=self.correct_creds_dict,
                follow_redirects=True
            ).request.path == self.image
            # Successful authentication adds the username to the session.
            assert wsgi.session['username'] == self.correct_creds[0]

    def test_login_invalid(self):
        ''' prevents invalid user logins '''
        ###############################################################################
        #
        # Test Requirements (invalid logins):
        #
        # Ensure invalid users are NOT able to log into the app.
        #
        # 1.) Send a POST request to the login route (self.login).
        #     - Include invalid credentials (self.invalid_creds_dict) in the request body.
        # 2.) Ensure the route handler does not add a username key to the session object.
        # 3.) Ensure the response body contains the case insensitive text: Login failed.
        ###############################################################################
        with wsgi.app.test_client() as client:
            # With invalid creds.
            assert b'login failed.' in client.post(
                self.login,
                data=self.invalid_creds_dict,
                follow_redirects=True
            ).data.lower()

            # Nothing should be added to the session.
            assert not wsgi.session.keys()

    def test_login_get(self):
        ''' ensure accessible login form '''
        ###############################################################################
        #
        # Test Requirements (login form):
        #
        # Ensure the login form contains the required username and password fields.
        #
        # 1.) Send a GET request to the login route (self.login).
        # 2.) Ensure the response body contains the case insensitive text:
        #     - username
        #     - password
        # 3.) Ensure the response status code is 200.
        ###############################################################################
        with wsgi.app.test_client() as client:
            # Should direct to the login page with a login form.
            response = client.get(self.login)
            assert response.status_code == 200
            # The login page contains input fields with the names: username and password.
            assert b'username' in response.data.lower()
            assert b'password' in response.data.lower()

    def test_logout(self):
        ''' can logout users '''
        ###############################################################################
        #
        # Test Requirements (logout):
        #
        # Ensure the logout process removes the user from the session.
        #
        # 1.) Simulate logging into the app by adding a username key to the session with a value of admin.
        #     - NOTE: The client.session_transaction() callable can be used to access a session
        #             before a request is made to the server.
        # 2.) Send a GET request to the logout route (self.logout).
        # 3.) Ensure the username key has been removed from wsgi.session.
        ###############################################################################
        with wsgi.app.test_client() as client:
            # Simulate an authenticated user.
            # The session_transaction method provides a context for a
            # session. Adding a username manually is similar to logging in.
            with client.session_transaction() as session:
                session['username'] = self.correct_creds[0]

            # Make a GET request to the logout route.
            client.get(self.logout)
            # Ensure the username key is not in the session.
            assert 'username' not in wsgi.session

class Index(WSGI.WSGIBase):
    def test_index_redirection_non_auth(self):
        ''' index page redirection '''
        ###############################################################################
        #
        # Test Requirements (index page redirection):
        #
        # Ensure unauthenticated users are redirected to the login route.
        #
        # 1.) Send a GET request to the index route (self.index).
        # 2.) Ensure the response redirects to the login route (self.login).
        ###############################################################################
        # Add test code below
        with wsgi.app.test_client() as client:
            response = client.get(self.index, follow_redirects=False)
            # Should redirect to login
            assert response.status_code == 302
            assert response.headers['Location'].endswith(self.login)
        # End test code
        ###############################################################################

    def test_index_redirection_auth(self):
        ''' index page redirection '''
        ###############################################################################
        #
        # Test Requirements (index page redirection):
        #
        # Ensure authenticated users are redirected to the image route.
        #
        # 1.) Simulate logging into the app by adding a username key to the session with
        #     a value of admin.
        # 2.) Send a GET request to the index route (self.index).
        # 3.) Ensure the response redirects to the image route (self.image).
        ###############################################################################
        # Add test code below
        with wsgi.app.test_client() as client:
            with client.session_transaction() as session:
                session['username'] = self.correct_creds[0]

            response = client.get(self.index, follow_redirects=False)
            # Should redirect to /image/
            assert response.status_code == 302
            assert response.headers['Location'].endswith(self.image)
        # End test code
        ###############################################################################

class ImageIntegration(WSGI.WSGIBase):

    # def test_image_post(self):
    #     ''' can upload images '''
    #     ###############################################################################
    #     #
    #     # Test Requirements (image route / authenticated):
    #     #
    #     # Ensure authenticated users can upload image files and view the results.
    #     #
    #     # 1.) Simulate  logging into the app by adding a username key to the session with
    #     #     a value of admin.
    #     # 2.) Send a POST request to the image route (self.image).
    #     #     - The post body must upload the IMAGE_FILE using the form field named: image.
    #     # 3.) Ensure the blurred image exists in the FILE_UPLOAD_FOLDER.
    #     #     - The hash produced from applying the blur effect to the IMAGE_FILE is:
    #     #       - 761b6b1329a80edc7a9b3a63a0455b64d23512b168bf0a5d8defde29.png
    #     # 4.) Ensure the response status code is 200.
    #     # 5.) Ensure the response redirects to the singular image route.
    #     #     - Example: /image/761b6b1329a80edc7a9b3a63a0455b64d23512b168bf0a5d8defde29.png
    #     # 6.) Ensure the filename is included in the response body.
    #     ###############################################################################
    #     with wsgi.app.test_client() as client:
    #         with client.session_transaction() as session:
    #             session['username'] = self.correct_creds[0]
    #
    #         # Omitting the effect form field defaults to blur
    #         with IMAGE_FILE.open('rb') as img:
    #             response = client.post(self.image, data={
    #                 'image': img,
    #             }, follow_redirects=True)
    #
    #         # filename is determined by passing the modified file's bytes
    #         # to the effects.file_id function.
    #         filename = '761b6b1329a80edc7a9b3a63a0455b64d23512b168bf0a5d8defde29.png'
    #         filepath = Path(wsgi.app.config['FILE_UPLOAD_FOLDER'])
    #         # Path makes it easy to check for files
    #         assert (filepath / filename).exists()
    #         # Ensure the image.html template includes a link to the file.
    #         assert response.status_code == 200
    #         assert response.request.path == f'{self.image}{filename}'
    #         assert filename.encode() in response.data

    # def test_image_get_all(self):
    #     ''' can display all images '''
    #     ###############################################################################
    #     #
    #     # Test Requirements (view all images):
    #     #
    #     # Ensure authenticated users can view all uploaded files.
    #     #
    #     # 1.) Simulate  logging into the app by adding a username key to the session with
    #     #     a value of admin.
    #     # 2.) Send a POST request to the image route (self.image) uploading the IMAGE_FILE
    #     #     and applying the blur effect.
    #     # 3.) Send a POST request to the image route (self.image) uploading the IMAGE_FILE
    #     #     and applying the mode effect.
    #     # 4.) Send a GET request to the image route (self.image):
    #     #     - Ensure the response status code is 200.
    #     #     - Ensure the following file names exist in the response body:
    #     #       - 761b6b1329a80edc7a9b3a63a0455b64d23512b168bf0a5d8defde29.png
    #     #       - 0118740a018bd0f7ebdae468e2ce845779c05630a513c6d418b57332.png
    #     ###############################################################################
    #     # Add test code below
    #     with wsgi.app.test_client() as client:
    #         with client.session_transaction() as session:
    #             session['username'] = self.correct_creds[0]
    #
    #         # Upload blur
    #         with IMAGE_FILE.open('rb') as img:
    #             client.post(self.image, data={'image': img}, follow_redirects=True)
    #
    #         # Upload mode
    #         with IMAGE_FILE.open('rb') as img:
    #             client.post(self.image, data={'image': img, 'effect': 'mode'}, follow_redirects=True)
    #
    #         response = client.get(self.image)
    #         assert response.status_code == 200
    #
    #         # Expect blurred and mode-hash images in response
    #         assert b'761b6b1329a80edc7a9b3a63a0455b64d23512b168bf0a5d8defde29.png' in response.data
    #         assert b'0118740a018bd0f7ebdae468e2ce845779c05630a513c6d418b57332.png' in response.data
    #     # End test code
    #     ###############################################################################

    def test_image_no_auth(self):
        ''' image route auth enforced '''
        ###############################################################################
        #
        # Test Requirements (image route / unauthenticated):
        #
        # Ensure unauthenticated requests are redirected to the login route.
        #
        # 1.) Send a GET request to the image route (self.image).
        #     - Ensure the response redirects to the login route (self.login).
        # 2.) Send a POST request to the image route (self.image).
        #     - Include the IMAGE_FILE.
        #     - Ensure the response redirects to the login route (self.login).
        ###############################################################################
        # Add test code below

        # End test code
        ###############################################################################

class CustomErrors(WSGI.WSGIBase):

    def test_404(self):
        ''' custom 404 page loads '''
        ###############################################################################
        #
        # Test Requirements (custom 404):
        #
        # Ensure the custom 404 error page is displayed for non-existent routes.
        #
        # 1.) Simulate  logging into the app by adding a username key to the session with
        #     a value of admin.
        # 2.) Send a GET request to the non-existent route: /404/
        # 3.) Ensure the following case insensitive bytestr exists in the response body:
        #     - image filter
        # 4.) Ensure the response status code is 404.
        ###############################################################################
        # Add test code below
        with wsgi.app.test_client() as client:
            with client.session_transaction() as session:
                session['username'] = self.correct_creds[0]

            response = client.get('/404/')
            assert response.status_code == 404
            assert b'image filter' in response.data.lower()
        # End test code
        ###############################################################################

    def test_500(self):
        ''' custom 500 page loads '''
        ###############################################################################
        #
        # Test Requirements (custom 500):
        #
        # Ensure the custom 500 error page is displayed for server side errors.
        #
        # 1.) Simulate  logging into the app by adding a username key to the session with
        #     a value of admin.
        # 2.) Send a POST request to the image route (self.image).
        #     - Include the IMAGE_FILE.
        #     - Include a non-existent effect:
        #       - fake
        # 3.) Ensure the following case insensitive bytestr exists in the response body:
        #     - image filter
        # 4.) Ensure the response status code is 500.
        ###############################################################################
        # Add test code below
        with wsgi.app.test_client() as client:
            with client.session_transaction() as session:
                session['username'] = self.correct_creds[0]

            with IMAGE_FILE.open('rb') as img:
                response = client.post(self.image, data={
                    'image': img,
                    'effect': 'fake'
                })

            assert response.status_code == 500
            assert b'image filter' in response.data.lower()
        # End test code
        ###############################################################################

    def test_InvalidImageError(self):
        ''' custom InvalidImageError page loads '''
        ###############################################################################
        #
        # Test Requirements (InvalidImageError handler):
        #
        # Ensure that InvalidImageError exceptions return a custom error page.
        #
        # 1.) Simulate  logging into the app by adding a username key to the session with
        #     a value of admin.
        # 2.) Send a POST request to the image route (self.image).
        #     - Include a non-image file to cause an InvalidImageError exception.
        #       - NOTE: The current code file works well: Path(__file__)
        # 3.) Ensure the following case insensitive bytestr exists in the response body:
        #     - gnome
        # 4.) Ensure the response status code is 500.
        ###############################################################################
        # Add test code below
        with wsgi.app.test_client() as client:
            with client.session_transaction() as session:
                session['username'] = self.correct_creds[0]

            with Path(__file__).open('rb') as fake_img:
                response = client.post(self.image, data={'image': fake_img})

            assert response.status_code == 500
            assert b'gnome' in response.data.lower()
        # End test code
        ###############################################################################

