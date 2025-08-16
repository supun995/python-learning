"""
The new_callable keyword argument of the patch callable specifies a callable to replace the default unittest.mock.MagicMock callable.
The patch callable calls the new_callable and uses the return value as the replacement object.
"""

from io import StringIO
from unittest.mock import patch
def greeter(name: str):
    ''' A function used to demonstrate the use of the patch callable. '''
    print(f'Hello, {name}')
# StringIO is an in-memory text stream that can replace standard output for testing.
# https://docs.python.org/3.9/library/io.html#io.StringIO
with patch(f'sys.stdout', new_callable=StringIO) as stdout_mock:
    ''' The keyword argument 'new_callable' replaces the default callable: unittest.mock.MagicMock. '''
    greeter('World')
    # stdout_mock is a StringIO object containing the text that was passed to print by the greeter function.
    assert stdout_mock.getvalue() == 'Hello, World\n' # \n is an end of line character.
###############################################################################
print('No assertion errors')
