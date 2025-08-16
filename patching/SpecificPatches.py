"""
Specific types of patches exist for select use cases. Patch includes callables for
patching dictionaries
, opens in a new tab,
class attributes and methods
, opens in a new tab, and
multiple attributes
, opens in a new tab. These specific patch callables can be used as context managers and decorators.
"""

import unittest
from unittest.mock import call, patch
##################### Patching Class Attributes & Methods #####################
class KeepingItClassy:
    class_attribute = print
    @classmethod
    def class_method(cls, *args):
        ...
# Patch class: attributes & methods
with patch.object(KeepingItClassy, 'class_method') as class_method_mock:
    # The class method has been replaced by a magic mock.
    KeepingItClassy.class_method(1, 2, 3)
    class_method_mock.assert_called_with(1, 2, 3)
with patch.object(KeepingItClassy, 'class_attribute') as class_attr_mock:
    # The class attribute has been replaced by a magic mock.
    KeepingItClassy.class_attribute('hello')
    class_attr_mock.assert_called_with('hello')
############################ Patching Dictionaries ############################
# Dictionary containing fake configuration data.
config = { 'hostname': 'prod.server.addr', 'port': 5001 }
# patch.dict can replace values in a dictionary for the scope of the patch.
with patch.dict(config, {'hostname': 'test.server.addr'}) as config_mock:
    assert config['hostname'] == 'test.server.addr'
    # This value remains unchanged.
    assert config['port'] == 5001
######################## Patching Multiple Attributes #########################
from unittest.mock import DEFAULT
import sqlite3
hostname = 'prod.server.addr'
database = sqlite3
if __name__ == '__main__':
    with patch.multiple('__main__', hostname=':memory:', database=DEFAULT) as replacements:
        # patch.multiple returns a dictionary.
        # Keys match the names of the patched attributes.
        database_mock = replacements['database']
        # Host name is replaced with a new str for the scope of this patch.
        assert hostname == ':memory:'
        # DEFAULT creates a mock using the default mock type.
        database_mock.connect(hostname)
        # Confirm that connect was called.
        database_mock.connect.assert_called_with(hostname)
###############################################################################
print('No assertion errors')