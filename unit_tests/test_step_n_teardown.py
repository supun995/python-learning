"""
Test cases may consist of many test methods. To reduce repeated code the TestCase base class includes setup and teardown methods. These methods are run before each test allowing tests to use shared resources.

This is commonly used to set up connections to external services such as databases.


"""

import unittest
import sqlite3
class TestSetupTeardown(unittest.TestCase):
    def setUp(self):
        ''' Actions to take before running each test. '''
        # Create a connection to a SQLite database.
        # This instance is an in-memory only instance.
        #
        # Each time a connection is created the database will be empty.
        self.db_connection = sqlite3.connect(':memory:')
        #
        curs = self.db_connection.cursor()
        # Create a database table named greeting with a single text column called name.
        curs.execute("CREATE TABLE greeting (name text);")
        # Commit to the changes.
        self.db_connection.commit()
    def tearDown(self):
        ''' Actions to take after running each test. '''
        # Close the connection to the database.
        # Which may be superfluous for an in-memory database.
        self.db_connection.close()
    def test_row_insert(self):
        expect = 'Hello'
        # setUp runs before this method and binds the database connection to the db_connection attribute.
        curs = self.db_connection.cursor()
        # Insert the word 'Hello' into the name column of the greeting table.
        curs.execute("INSERT INTO greeting VALUES (?);", (expect,))
        # Commit to the changes.
        self.db_connection.commit()
        # Fetch the newly inserted row and extract the first (and only) column.
        actual = curs.execute("SELECT name FROM greeting;").fetchone()[0]
        # Assert that the greeting returned is the same as the greeting written to the DB.
        self.assertTrue(expect == actual)
    def test_starts_empty(self):
        # setUp runs before this method and binds the database connection to the db_connection attribute.
        curs = self.db_connection.cursor()
        # The fetchone method will return None if no data is returned from the DB.
        self.assertIsNone(curs.execute("SELECT name FROM greeting;").fetchone())
if __name__ == '__main__':
    unittest.main()