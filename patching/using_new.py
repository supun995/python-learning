from unittest.mock import patch
def user_choice(prompt):
    return input(prompt)
with patch(f'builtins.input', new=lambda _prompt: 3):
    '''
        The keyword argument 'new' replaces the target with an object. 
        In this example the object is a lambda function.
        The lambda function is a shorthand for the following:
        >>> def fake_input(_prompt):
        ...    return 3 
        The unused _prompt parameter is included for context.
    '''
    # The builtin input callable will be replaced inside this code block.
    # The lambda function used to replace input is hardcoded to return 3.
    assert user_choice('select a number between 1 and 10') == 3
###############################################################################
print('No assertion errors')
