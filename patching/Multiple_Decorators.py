from unittest.mock import patch
def greeter():
    name = input("What's your name? ")
    print(f'Hello, {name}')
@patch(f'builtins.print')
@patch(f'builtins.input')
def test_stacks(input_mock, print_mock):
    # The patch decorators pass mocked objects as input parameters.
    # Python runs decorators from the bottom up.
    # The order of the input parameters match.
    input_mock.return_value = 'World'
    # Running greeter will call input and print.
    greeter()
    # Verify the calls
    input_mock.assert_called_once()
    print_mock.assert_called_with('Hello, World')
test_stacks()
###############################################################################
print('No assertion errors')
