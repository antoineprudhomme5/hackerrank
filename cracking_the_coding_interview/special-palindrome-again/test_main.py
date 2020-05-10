import unittest

from main import substr_count


class TestMain(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(substr_count(8, 'mnonopoo'), 12)

    def test_case_2(self):
        self.assertEqual(substr_count(5, 'asasd'), 7)

    def test_case_3(self):
        self.assertEqual(substr_count(7, 'abcbaba'), 10)

    def test_case_4(self):
        self.assertEqual(substr_count(4, 'aaaa'), 10)


if __name__ == '__main__':
    unittest.main()
