"""
The
unittest.TestCase
, opens in a new tab base class defines methods for performing assertions. These methods are used to compare and inspect objects in different ways.

Examples:

assertTrue
assertFalse
assertNone
assertEqual
Complete Documentation
, opens in a new tab
Tests use one or more of these assertion methods to test assumptions.
"""

import unittest
class Test(unittest.TestCase):
    def test_common_assertion_methods(self):
        ''' A non-exhaustive demonstration of many of the common methods
            The unittest.TestCase class provides methods for different types of assertions.
        '''
        # Compare any two objects using the assertEqual method.
        # A method version of the == operator.
        self.assertEqual('hey', 'hey')
        # With a message
        # All assert* methods allow a message to be provided.
        # The message is displayed in the test runner if the assertion is false.
        # The message argument is omitted in the remaining examples for brevity.
        self.assertEqual(1, 1, 'there has been a disturbance in the force.')
        # Compare any two objects using the assertNotEqual method.
        # A method version of the != operator.
        self.assertNotEqual('hey', 'sup')
        # Check the `truthiness` of an object using assertTrue.
        self.assertTrue('hey' == 'hey')
        # Check the `truthiness` of an object using assertFalse.
        self.assertFalse('hey' == 'sup')
        # Check the identity of an object using assertIs.
        # A method version of the `is` operator.
        greeting_a = 'hey'
        greeting_b = greeting_a
        # Do both name bindings reference the same object in memory?
        # Yes. Same str
        self.assertIs(greeting_a, greeting_b)
        # Check the identity of an object using assertIsNot.
        greeting_a = 'hey'
        greeting_b = 'sup'
        # Do both name bindings reference the same object in memory?
        # No, since they're two different strs.
        self.assertIsNot(greeting_a, greeting_b)
        # Check if an expression evaluates to None using the assertIsNone.
        # Hardcoded None
        self.assertIsNone(None)
        # Expression
        self.assertIsNone(1 == 2 or None)
        # Since 1 does not equal 2 None is returned.
        # Check if an expression evaluates to something other than None using the assertIsNotNone.
        self.assertIsNotNone(1 == 2)
        # Check if an object exists inside a collection using the assertIn.
        self.assertIn(3, [1,2,3,4,5,6])
        # Check if an object does not exist inside a collection using the assertNotIn.
        self.assertNotIn(7, [1,2,3,4,5,6])
        # Check if an object is a specific instance of a class using the assertIsInstance.
        self.assertIsInstance('hey', str)
        self.assertIsInstance(12345, int)
        # Example with a user defined class:
        class Hey: ...
        self.assertIsInstance(Hey(), Hey)
        # Check if an object is not a specific instance of a class using the assertNotIsInstance.
        self.assertNotIsInstance('hey', int)
        self.assertNotIsInstance(12345, str)
        # Example with a user defined class:
        class Hey: ...
        self.assertNotIsInstance(Hey(), str)
        # Check if a callable raises a specific exception using the assertRaises.
        # This assert is a bit different from the others in that a callable is passed as an argument.
        # `int` is the callable that will be run.
        # Arguments to the right of the callable are passed to the callable.
        # This is similar to:
        # int('not a number')
        # Which raises a ValueError
        self.assertRaises(ValueError, int, 'not a number')
if __name__ == '__main__':
    unittest.main()