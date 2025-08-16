import unittest
from playground import userman


class UserManager(unittest.TestCase):
    def setUp(self):
        self.um = userman.UserManagement()
        self.username = 'admin'
        self.password = 'magic'

    def test_upsert_user_insert(self):
        ''' can insert new users '''
        ###############################################################################
        #
        # Test Requirements (UserManagement.upsert_user):
        #
        # The UserManagement.upsert_user method accepts a username and password as input and
        # inserts or updates the creds dictionary accordingly.
        #
        # Inserting new users must normalize the username to lowercase to ensure
        # a standard is applied and save the password.
        #
        # 1.) Ensure the upsert_user method normalizes usernames as lowercase.
        # 2.) Ensure the upsert_user method adds passwords to the creds attribute.
        ###############################################################################
        # No users should exist on init.
        assert not self.um.creds.keys()
        # Add a user with a title cased username. Upsert_user should normalize it.
        self.um.upsert_user(self.username.title(), self.password)
        # Ensure the user is added with a lowercase normalized name.
        assert self.username in self.um.creds
        # Ensure the creds aren't blank. Checking the value happens elsewhere.
        assert self.um.creds[self.username]

    def add_user(self, username=None, password=None):
        self.um.upsert_user(
            username or self.username,
            password or self.password
        )


    def test_upsert_user_update(self):
        ''' can update existing user '''
        ###############################################################################
        #
        # Test Requirements (UserManagement.upsert_user):
        #
        # Updating the password for existing users must change the password.
        #
        #
        # The UserManagement.upsert_user method accepts a username and password as input and
        # inserts or updates the creds dictionary accordingly.
        #
        # 1.) Ensure the upsert_user method updates passwords for existing users.
        ###############################################################################
        self.add_user()
        before = self.um.creds[self.username]
        self.um.upsert_user('admin', 'x')
        after = self.um.creds[self.username]
        assert before != after
        assert after == 'x'

    def test_creds_for(self):
        ''' can get creds by username '''
        self.add_user()
        ###############################################################################
        #
        # Test Requirements (UserManagement.creds_for):
        #
        # The UserManagement.creds_for method accepts a username as input and
        # returns the user's password - if the user exists. An UnknownUser exception
        # is raised if the user does not exist.
        #
        # 1.) Ensure the creds_for method returns a non-None value for existing users.
        # 2.) Ensure the creds_for method raises an UnknownUser exception for non-existent users.
        ###############################################################################
        # Add test code below
        self.assertEqual(self.um.creds_for(self.username), self.password)

        with self.assertRaises(userman.UnknownUser):
            self.um.creds_for("ghost")
        # End test code
        ###############################################################################

    def test_authenticate(self):
        ''' can authenticate valid users '''
        self.add_user()
        ###############################################################################
        #
        # Test Requirements (UserManagement.authenticate):
        #
        # The UserManagement.authenticate method accepts a username and password
        # as input and returns a boolean value indicating if the username exists and
        # the passwords match.
        #
        # 1.) Ensure the authenticate method normalizes usernames to lowercase.
        #     - Usernames are not case sensitive.
        # 2.) Ensure the authenticate method returns True for matching username/password combinations.
        # 3.) Ensure the authenticate method returns False for non-existent users.
        # 4.) Ensure the authenticate method returns False for incorrect passwords.

        ###############################################################################
        # Add test code below
        # 1 & 2: case-insensitive match
        self.assertTrue(self.um.authenticate("admin", self.password))
        self.assertTrue(self.um.authenticate("ADMIN", self.password))

        # 3: non-existent user
        self.assertFalse(self.um.authenticate("ghost", "whatever"))

        # 4: wrong password
        self.assertFalse(self.um.authenticate(self.username, "wrong"))
        # End test code
        ###############################################################################
