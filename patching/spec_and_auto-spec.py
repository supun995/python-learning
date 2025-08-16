"""
Mock objects create attributes and methods on-demand giving them the ability to replace other objects.
Allowing for maximum flexibility, mocks don't enforce restrictions on allowed attributes or callable parameters.
These allowed differences can lead to tests which are tightly coupled to mock objects rather than the objects being mocked.

The unittest.mock module includes a mechanism called spec which is used to ensure mock objects adhere more closely to the object being mocked.

The spec keyword argument of the patch callable passes the argument through to the spec argument of the default mock callable.

Spec is useful for ensuring that mocks include the same attributes and methods as the provided object.
 However, spec allows callables to be called with any arguments without considering the defined parameters of the callable.
  The auto-spec feature enforces call signatures.

The below code demonstrates the difference between spec and autospec.
"""
from unittest.mock import patch
class KeepingItClassy:
    def add(self, a, b):
        return self.a + self.b
if __name__ == '__main__':
    # Spec
    with patch(f'__main__.KeepingItClassy', spec=KeepingItClassy) as keep_it_classy_mock:
        ''' The keyword argument 'spec' passes the argument to unittest.mock.MagicMock. '''
        keep_it_classy_mock.add.return_value = 2
        assert keep_it_classy_mock.add(1, 1) == 2
        keep_it_classy_mock.add.assert_called_with(1, 1)
        keep_it_classy_mock.add.assert_called_once()
        try:
            # Attempt to access a non-existent attribute.
            keep_it_classy_mock.non_existent_attr
        except AttributeError:
            print(
                'Spec matches the attributes of the patched object.\n'
                'Non-existent attributes raise an AttributeError exception when accessed.'
            )
        # spec doesn't enforce method signatures.
        # Calling add would result in a TypeError if this was the real KeepingItClassy
        assert keep_it_classy_mock.add() == 2
        keep_it_classy_mock.add.assert_called_with()
    # Auto-spec
    with patch(f'__main__.KeepingItClassy', autospec=True) as keep_it_classy_mock:
        ''' The keyword argument 'autospec' conforms to the structure of the mocked object. '''
        keep_it_classy_mock.add.return_value = 2
        assert keep_it_classy_mock.add(1, 1) == 2
        keep_it_classy_mock.add.assert_called_with(1, 1)
        keep_it_classy_mock.add.assert_called_once()
        try:
            # Attempt to access a non-existent attribute.
            keep_it_classy_mock.non_existent_attr
        except AttributeError:
            print(
                'Auto-spec matches the attributes of the patched object.\n'
                'Non-existent attributes raise an AttributeError exception when accessed.'
            )
        try:
            keep_it_classy_mock.add()
        except TypeError:
            print('Auto-spec enforces method signatures.')
###############################################################################
print('No assertion errors')
