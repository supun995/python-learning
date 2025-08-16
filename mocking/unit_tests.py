import random
import unittest
from unittest.mock import Mock
# Imagine that this connects out to some external source and returns resource info.
def resource_finder(ref: str, source: str) -> dict:
    return {'ref': ref, 'source': source, 'price': random.random() * random.randint(1, 10) }
class PriceLocator:
    def price_of(self, ref: str, source: str, finder: callable = resource_finder) -> float:
        ''' Simulate returning a price for a fake resource. '''
        return finder(ref, source)['price']
class PriceLocatorTestCase(unittest.TestCase):
    def test_price_of(self):
        # Setup the finder callable's method arguments.
        ref, source = 'abc123', 'amazon.com'
        price = PriceLocator()
        # External resources are not always fast, predictable, or reliable.
        # Replacing external resources inside unit tests with mocks makes tests faster and more reliable.
        # In this test knowing that the finder callable is provided with the correct arguments
        # is more important than connecting to the "external service" simulated with resource_finder.
        # This allows the price_of method to be tested independently of dependent services.
        #
        # Create a mock to replace the callable-finder argument of the price_of method.
        finder = Mock(return_value={'ref': ref, 'source': source, 'price': 3.14 })
        # Ensure the correct price is returned.
        assert price.price_of(ref, source, finder) == 3.14
        # Ensure the finder callable was called with the expected arguments.
        finder.assert_called_with(ref, source)
if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)
