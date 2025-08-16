"""
Test methods can be conditionally skipped using decorator functions or TestCase methods.
This is useful in scenarios where tests aren't required for a given operating system, Python version, module version, etc.
"""

import unittest
import sys
class TestSkipIt(unittest.TestCase):
    @unittest.skip('always skipped')
    def test_skip(self):
        self.fail('will not run because test is skipped.')
    # Skip a test unless a condition is met.
    @unittest.skipIf(sys.version_info.major >= 3, 'Python 2 only.')
    def test_skip_if(self):
        self.fail('will not run because test is skipped.')
    # Skip a test unless a condition is met.
    @unittest.skipUnless(sys.platform.startswith('win'), 'Windows only test.')
    def test_skip_unless(self):
        self.fail('will not run because test is skipped.')
    # Conditionally skip a test method from inside the test.
    def test_possibly_skip(self):
        if True:
            self.skipTest('skip based on some condition')
        # If not skipped then perform some test.
        self.assertTrue(True)
    # This test will run.
    def test_is_number(self):
        # Ensure that str objects which represent ints are correctly converted to int.
        self.assertTrue(int('10') == 10)
        # Ensure that other valid int representations produce ints.
        # For example int literals allow underscores for added readability.
        self.assertTrue(int('1_000') == 1_000)
        # Numbers represented in base 2 (binary) are ints too.
        # Change the base number system to 2 and check
        self.assertTrue(int('011', base=2) == 3)
if __name__ == '__main__':
    unittest.main()
