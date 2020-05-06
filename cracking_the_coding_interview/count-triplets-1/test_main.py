import unittest

from main import count_triplets


class TestMain(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(count_triplets([1, 2, 2, 4], 2), 2)

    def test_case_2(self):
        self.assertEqual(count_triplets([1, 3, 9, 9, 27, 81], 3), 6)

    def test_case_3(self):
        self.assertEqual(count_triplets([1, 5, 5, 25, 125], 5), 4)


if __name__ == '__main__':
    unittest.main()
