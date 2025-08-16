class UnknownUser(Exception):
    ''' Exception raised if a username is not found. '''

class UserManagement:
    ''' Fake user management system.  '''

    def __init__(self):
        self.creds = {}

    def upsert_user(self, username, password):
        self.creds[username.lower()] = password

    def creds_for(self, username):
        try:
            return self.creds[username.lower()]
        except KeyError:
            raise UnknownUser(f'Authentication for {username} failed.')

    def authenticate(self, username, password) -> bool:
        try:
            creds = self.creds_for(username)
        except UnknownUser:
            return False
        except:
            raise

        return creds == password