"""
Mock records all calls made along with arguments. Assertion methods can make claims about how calls are made. However, they're unable to provide detailed insights into calls.

Mocks include attributes used to access more detailed call information.

The unittest.mock module includes a helper object named
call
, opens in a new tab used as a means of creating calls for comparison against recorded calls. Providing call the same arguments provided to a mock call makes the two calls comparable.

The below code demonstrates how to interact with recorded calls.


"""

from unittest.mock import call, Mock
############################### Inspecting Calls ##############################
#
fake_object = Mock()
#
# Call with positional and keyword arguments.
fake_object('hi', 'there', who='world')
# Call without arguments.
fake_object()
# The call_count attribute reflects the number of calls made to the mock.
assert fake_object.call_count == 2
# Inspecting calls more closely is done with the unittest.mock.call object.
# Call makes it easier to make assertions regarding how the mock was called.
#
# Comparisons can be made by providing the same arguments to call that were
# provided to the mock.
#
# The calls to fake_object produce the following list of calls.
expected_calls = [call('hi', 'there', who='world'), call()]
# The assert_has_calls ensures that calls made to mock match what's expected.
# By default the order of the calls must match the order they were called.
fake_object.assert_has_calls(expected_calls)
# The any_order keyword argument ignores the call order.
fake_object.assert_has_calls(expected_calls, any_order=True)
# The call_args_list attribute stores the calls made to the mock in the
# order they were called.
assert fake_object.call_args_list == expected_calls
# Call the mock again so that this is the last call made.
fake_object('a', 'z', lang='en', case='lower')
# The call_args attribute stores the arguments of the last call as a tuple.
# The first element contains positional arguments.
# The second element contains keyword arguments.
assert fake_object.call_args == (('a', 'z'), { 'lang': 'en', 'case': 'lower' })
# Specific elements are accessible by name.
assert fake_object.call_args.args == ('a', 'z')
assert fake_object.call_args.kwargs == { 'lang': 'en', 'case': 'lower' }
# Mock doesn't record method calls in the call_args_list attribute.
# Calling a mock method.
fake_object.fake_attribute.fake_method("a")
# The method_calls attribute displays only method calls and not calls
# made directly to the mock object.
assert fake_object.method_calls == [call.fake_attribute.fake_method("a")]
# The mock_calls attribute displays all calls.
assert fake_object.mock_calls == [
    call("hi", "there", who="world"),
    call(),
    call("a", "z", lang="en", case="lower"),
    call.fake_attribute.fake_method("a"),
]
###############################################################################
print('No assertion errors')