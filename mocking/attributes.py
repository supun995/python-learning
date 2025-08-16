"""
Mock objects allow attributes to be set when created using keyword arguments. Attributes can also be set after an object is created.

Mocks create attributes dynamically when accessed if they don't already exist. Removed attributes are not dynamically recreated on subsequent attempts to access.
"""

from unittest.mock import Mock
def connection(db):
    ''' A function used to demonstrate conditional attribute access. '''
    if hasattr(db, 'connection_source'):
        return db.connection_source
    return 'xyz'
# Attributes can be set by specifying attribute names as keyword arguments.
mock = Mock(connection_source='abc', hostname='localhost')
assert mock.connection_source == 'abc'
assert mock.hostname == 'localhost'
# Attributes can also be set directly on the mock object.
mock.another_attribute = 3.14
assert mock.another_attribute == 3.14
# Attempting to access a non-existent attribute will dynamically create it.
# Attributes are mock objects.
# Assert that the created attribute exists
assert mock.now_i_exist
# The connection function checks for an attribute named
# connection_source on the provided object.
# If the attribute exists it's returned, otherwise 'xyz' is returned.
assert connection(mock) == 'abc'
# Remove the connection_source attribute from the mock.
del mock.connection_source
# The connection function will return xyz now that the connection_source
# attribute is set.
assert connection(mock) == 'xyz'
try:
    # Attempting to access the attribute now will raise an AttributeError.
    # Mock doesn't dynamically re-add the attribute when accessed
    # after the attribute is deleted.
    mock.connection_source
except AttributeError as ex:
    print(f'The {ex.args[0]} attribute does not exist')
# Removed attributes can be re-added by setting them directly.
mock.connection_source = 'welcome back'
assert mock.connection_source == 'welcome back'
###############################################################################
print('No assertion errors')