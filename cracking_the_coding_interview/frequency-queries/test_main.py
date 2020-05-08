import unittest

from main import frequency_queries


class TestMain(unittest.TestCase):

    def test_case_1(self):
        queries = [
            [1, 5],
            [1, 6],
            [3, 2],
            [1, 10],
            [1, 10],
            [1, 6],
            [2, 5],
            [3, 2]
        ]
        self.assertEqual(frequency_queries(queries), [0, 1])

    def test_case_2(self):
        queries = [
            [3, 4],
            [2, 1003],
            [1, 16],
            [3, 1]
        ]
        self.assertEqual(frequency_queries(queries), [0, 1])

    def test_case_3(self):
        queries = [
            [1, 3],
            [2, 3],
            [3, 2],
            [1, 4],
            [1, 5],
            [1, 5],
            [1, 4],
            [3, 2],
            [2, 4],
            [3, 2],
        ]
        self.assertEqual(frequency_queries(queries), [0, 1, 1])

if __name__ == '__main__':
    unittest.main()
