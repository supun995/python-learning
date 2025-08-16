"""
The patch callable can be used as a callable decorator.
The patch remains in effect for the duration of the patched callable.
Decorators pass replacement objects as arguments to decorated callables.
"""

from unittest.mock import patch
def greeter(name: str):
    ''' A function used to demonstrate the use of the patch callable. '''
    print(f'Hello, {name}')
# Replace the built-in print function with a Mock for this function only.
@patch(f'builtins.print')
def test_greeter(print_mock):
    # The patch decorator passes mocked objects as input parameters.
    #
    # With the print function replaced with a mock for the duration of
    # this method no data is printed to the console.
    greeter('World')
    # Inspect the mock version of the print function and determine if it
    # was provided with the expected input.
    print_mock.assert_called_with('Hello, World')
    print_mock.assert_called_once()
test_greeter()
###############################################################################
print('No assertion errors')
