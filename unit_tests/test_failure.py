import unittest
class TestFailures(unittest.TestCase):
    def test_failures(self):
        self.assertTrue(False, 'oh no!')
if __name__ == '__main__':
    unittest.main()