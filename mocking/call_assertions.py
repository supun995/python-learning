"""
Mocks record calls and provide different mechanisms for inspecting how calls were made.

Mock objects include methods used to make assertions about calls.
Assertion methods
, opens in a new tab raise an
AssertionError
, opens in a new tab for False assertions.

The below code demonstrates some common assertion methods.
"""

from unittest.mock import Mock

fake_object = Mock()

# The assert_not_called method ensures the mock was not called.
fake_object.assert_not_called()

# Call the mock object so that it can record the call.
fake_object('hi', 'there')

# The assert_called method ensures the mock was called at least once.
fake_object.assert_called()

# The assert_called_once method ensures the mock was called only once.
fake_object.assert_called_once()

# The assert_called_with method inspects the arguments passed to the mock the last time it was called.
fake_object.assert_called_with('hi', 'there')

# The assert_called_once_with method ensures the mock was called only once with the specified arguments.
fake_object.assert_called_once_with('hi', 'there')

# The reset_mock method clears recorded calls allowing the mock to be reused.
fake_object.reset_mock()
fake_object.assert_not_called()

###############################################################################
print('No assertion errors')