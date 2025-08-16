"""
The unittest module takes an object-oriented approach to testing;
introducing a base class used as a test building block called a test case.

Test cases define a context for performing tests.
Any concept which can be treated as a single unit can be a test case.
Including: functions, class definitions, workflows, etc.
Tests are defined by methods which start with the word test. Tests are located and run by the test runner.
"""

import unittest
class TestMethods(unittest.TestCase):
    def test_should_run(self):
        self.assertTrue(True)
    def wont_run(self):
        self.assertTrue(False)
if __name__ == '__main__':
    unittest.main()