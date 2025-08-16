from unittest.mock import Mock
################################### Repeated Calls ############################
# Repeated calls can return different values by specifying a list as the side_effect argument.
# The return order matches the order of the objects in the list.
mock = Mock(side_effect=['a', 'b', 'c'])
# Each call returns the next object in the list.
assert mock() == 'a'
assert mock() == 'b'
assert mock() == 'c'
# A StopIteration exception is raised when no values remain.
try:
    mock()
except StopIteration:
    print('Calling mock after all objects have been returned results in an error.')
##################################### Exceptions ##############################
# Calls can raise exceptions by specifying an exception as the side_effect argument.
mock = Mock(side_effect=Exception('Side effects can raise exceptions.'))
try:
    mock()
except Exception as ex:
    print(ex)
################################ Exceptions in Lists ##########################
# Exceptions inside a list are raised when encountered.
mock = Mock(side_effect=['a', 'b', Exception('Exceptions inside a list are raised when encountered.'), 'c'])
# The first two values...
assert mock() == 'a'
assert mock() == 'b'
try:
    # The third call encounters the exception and raises it.
    mock()
except Exception as ex:
    print(ex)
# Because the exception was handled the next call returns the next value.
assert mock() == 'c'
##################################### Functions ###############################
def multiplier(a, b):
    ''' multiply two numbers and return the result '''
    return a * b
# Side effects can be callables.
mock = Mock(side_effect=multiplier)
# Arguments passed to the mock are passed through to the callable.
assert mock(10, 10) == 100
###############################################################################
print('No assertion errors')