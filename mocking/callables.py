import random
from unittest.mock import Mock

################################## Callables ##################################
fake_object = Mock()

# Mocks can be called with any arguments.
fake_object('a', 'b', z=True)
fake_object(1, 2)
fake_object()

# Mocks dynamically create attributes and methods when accessed.
fake_object.fake_method()
fake_object.fake_method(1, 2, 3, 4)
fake_object.fake_method(z=True, x=False)

fake_object.fake_attribute.fake_method()
################################ Return Values ################################
#
# Mock objects can return predefined values.
#
## Keyword Argument
#
# The return_value argument specifies the value to return when the mock is called.
calc_pi = Mock(return_value=3.14159)

# Calls will now return the specified value.
assert calc_pi() == 3.14159

## Attribute
#
# The return_value attribute can be set after the mock is created.
calc_pi = Mock()

calc_pi.return_value = 3.14159

# Calls will now return the specified value.
assert calc_pi() == 3.14159

## Method Return Values
#
mock = Mock()

# The return_value attribute can be set on the mock method.
mock.fake_attribute.fake_method.return_value = 'method to the madness'

# Calls will now return the specified value.
assert mock.fake_attribute.fake_method() == 'method to the madness'
###############################################################################
print('No assertion errors')
