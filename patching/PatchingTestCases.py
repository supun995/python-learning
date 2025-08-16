"""
The patch callable is commonly used during testing.
Patch can decorate all or individual methods by applying the decorator to classes or methods.
"""

import unittest
from unittest.mock import call, patch
def greeter(name: str):
    ''' A function used to demonstrate the use of the patch callable. '''
    print(f'Hello, {name}')
def greet_everyone(*names):
    ''' A function used to demonstrate the use of the patch callable. '''
    for name in names:
        print(f'Hello, {name}')
############################## Patching Methods ###############################
#
class GreeterTest(unittest.TestCase):
    # Replace the built-in print function with a Mock for this method only.
    @patch(f'builtins.print')
    def test_greeter(self, print_mock):
        # The patch decorator passes mocked objects as input parameters.
        #
        # With the print function replaced with a mock for the duration of
        # this method no data is printed to the console.
        greeter('World')
        # Inspect the mock version of the print function and determine if it
        # was provided with the expected input.
        print_mock.assert_called_with('Hello, World')
        print_mock.assert_called_once()
############################## Patching Classes ###############################
#
# Replace the built-in print function for all methods of this class.
@patch(f'builtins.print')
class GreetEveryoneTest(unittest.TestCase):
    def test_greeter(self, print_mock):
        # The patch decorator passes mocked objects as input parameters.
        greeter('World')
        # Inspect the mock version of the print function and determine if it
        # was provided with the expected input.
        print_mock.assert_called_with('Hello, World')
        print_mock.assert_called_once()
    def test_greet_everyone(self, print_mock):
        # The patch decorator passes mocked objects as input parameters.
        greet_everyone('World', 'Universe', 'Multiverse', 'Ultraverse')
        # The expected calls made to the mock implementation of print.
        expect = [
            call('Hello, World'),
            call('Hello, Universe'),
            call('Hello, Multiverse'),
            call('Hello, Ultraverse'),
        ]
        # Ensure the calls made to print are passed the expected arguments.
        assert print_mock.mock_calls == expect
        assert print_mock.call_count == len(expect)
###############################################################################
if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)