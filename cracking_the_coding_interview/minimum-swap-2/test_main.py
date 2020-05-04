import unittest

from main import minimum_swaps

class TestMain(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(minimum_swaps([7, 1, 3, 2, 4, 5, 6]), 5)
    
    def test_case_2(self):
        self.assertEqual(minimum_swaps([4, 3, 1, 2]), 3)
    
    def test_case_3(self):
        self.assertEqual(minimum_swaps([2, 3, 4, 1, 5]), 3)


if __name__ == '__main__':
    unittest.main()
