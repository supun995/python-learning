"""
The
unittest.mock.patch
, opens in a new tab callable is used to replace objects for a limited scope. The patch callable can be used as a context manager or callable decorator. Patches remain in effect for the life of the context manager or decorated callable.

Patches are commonly used during testing to replace external resources with alternate implementations.

Key Features of Patches

Patches replace objects with
MagicMock
, opens in a new tab by default.
AsyncMock
, opens in a new tab is used when decorating async callables.
Patches can specify an object or callable as the replacement object.

"""
from unittest.mock import patch
def greeter(name: str):
    ''' A function used to demonstrate the use of the patch callable. '''
    print(f'Hello, {name}')
# Patch can be used as a context manager.
# The first argument is a target object to replace.
# The target is a str representing the package.module.object
with patch(f'builtins.print') as print_mock:
    # The builtin print callable will be replaced inside this code block.
    greeter('World')
    # Inspect the mock version of the print callable and determine if it
    # was provided with the expected input.
    print_mock.assert_called_with('Hello, World')
    print_mock.assert_called_once()
# Outside the context manager print behaves normally.
greeter('World')
###############################################################################
print('No assertion errors')