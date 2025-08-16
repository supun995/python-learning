"""
Mock objects create attributes and methods on-demand giving them the ability to replace other objects. Allowing for maximum flexibility, mocks don't enforce restrictions on allowed attributes or callable parameters. These allowed differences can lead to tests which are tightly coupled to mock objects rather than the objects being mocked.

The unittest.mock module includes mechanisms used to ensure mock objects adhere more closely to the object being mocked.


"""

from unittest.mock import MagicMock, create_autospec
class KeepingItClassy:
    def add(self, a, b):
        return self.a + self.b
    def mul(self, a, b):
        return self.a + self.b
# The spec keyword argument ensures mock matches the methods and attributes of
# a class or object.
mock = MagicMock(spec=KeepingItClassy)
# Set the return values for the two methods.
mock.add.return_value = 2
mock.mul.return_value = 10
# Calling the methods returns the expected pre-set return values.
assert mock.add(1, 1) == 2
assert mock.mul(5, 2) == 10
# Ensure the methods are called with the expected arguments.
mock.add.assert_called_with(1, 1)
mock.mul.assert_called_with(5, 2)
# Spec ensures that non-existent attributes and methods aren't created dynamically.
# Attempting to access a non-existent attributes raises an AttributeError.
try:
    mock.non_existent_attr
except AttributeError as ex:
    print(f'The {ex.args[0]} attribute does not exist')
# Attempting to access an non-existent method raises an AttributeError.
try:
    mock.div(10, 2)
except AttributeError as ex:
    print(f'The {ex.args[0]} attribute does not exist')
# Spec is useful for ensuring that attributes and methods match the given spec object.
# However, spec allows callables to be called with any arguments without considering
# the defined parameters of the callable.
# A function with 2 required positional arguments.
def add(a, b):
    return a + b
# Use the add function as the spec with a return value of 2.
mock = MagicMock(spec=add, return_value=2)
assert mock(1, 1) == 2
# The spec doesn't respect the 2 defined parameters.
mock(1, 1, 1)
# The create_autospec callable creates mocks that enforce callable signatures.
# create_autospec creates a MagicMock by default.
mock = create_autospec(spec=add, return_value=2)
assert mock(1, 1) == 2
# Trying to call the mock object with the incorrect signature results in an error.
try:
    mock(1, 1, 1)
except TypeError as ex:
    print(ex)
###############################################################################
print('No assertion errors')