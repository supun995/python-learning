"""

Test Runner CLI
The test runner can be started by invoking the unittest module as a command line application. Including options to run one or more test modules, test cases, or test methods.

Configuration can be specified using
command line flags
, opens in a new tab.

Copy code
python3 -m unittest -h
python3 -m unittest cloudacademy.test_assertion -v -f
"""

import unittest
class TestExample(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(int('10') == 10)
    def test_not_number(self):
        with self.assertRaises(ValueError):
            int('nope')
