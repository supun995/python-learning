"""
The
unittest.mock
, opens in a new tab module is Python's built-in mocking and patching module. Used to replace objects with fake implementations during testing.

Mock
, opens in a new tab objects -- or mocks -- can replace objects with fake implementations and make assertions about how mock objects are used.

Mocks are commonly used to replace objects and external resources such as files, databases, and web APIs.

Replacing functionality with mock implementations allows code to be tested independently of its dependencies.

Key Features of Mocks

Mocks are callable.
Non-callable varients exist:
NonCallableMock
, opens in a new tab
NonCallableMagicMock
, opens in a new tab
Mocks create attributes and methods when first accessed.
Mocks record all calls along with arguments.
Mocks include assertion methods used to ensure calls are made as expected.
Failed assertions raise an AssertionError
The following is a basic demonstration of unittest.mock.Mock. In this example a mock is used to replace Python's built-in print callable.



"""
from unittest.mock import Mock

def greeter(name: str, display_callable: callable = print):
    ''' Demo function used to demonstrate how to use a mock in place of another object.'''
    display_callable(f'Hello, {name}')

# This will display Hello, World in the console because the built-in print
# function is the default argument for the display_callable parameter.
greeter('World')
# Call again passing a mock as the display_callable.
display = Mock()
# This will not display in the console because the mock is called in
# place of the print function.
greeter('World', display)
# Mocks include different assertion methods used to determine if the
# mock implementation is called as expected.
# Verify that the mock implementation of print is called with the expected
# argument value.
display.assert_called_with('Hello, World')

###############################################################################
print('No assertion errors')

