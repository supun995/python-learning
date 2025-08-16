"""
The unittest module includes a mechanism for running tests called a test runner. The test runner is used to run one or more tests from one or more test cases.
"""

# import unittest
# ...
# # Q: What does __name__ == '__main__' do?
# # A: It determines if this code is being run directly.
# # Example: $ python3 code_file.py
# # It doesn't run if this code file is imported as a module.
# if __name__ == '__main__':
#     unittest.main()

import unittest
class TestExample(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(int('10') == 10)
    def test_not_number(self):
        with self.assertRaises(ValueError):
            int('nope')
if __name__ == '__main__':
    # Increase the verbosity of the console output and stop all tests after the first - if any -- assertion fails
    # Similar to using the CLI flags: python3 test_assertion.py -v -f
    unittest.main(verbosity=2, failfast=True)