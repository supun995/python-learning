import unittest
class TestExample(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(int('10') == 10)
    def test_not_number(self):
        with self.assertRaises(ValueError):
            int('nope') 
if __name__ == '__main__':
    unittest.main()