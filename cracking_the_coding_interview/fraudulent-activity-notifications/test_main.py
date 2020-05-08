import unittest

from main import activity_notifications


class TestMain(unittest.TestCase):
    def test_case_1(self):
        expenditures = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        self.assertEqual(activity_notifications(expenditures, 5), 2)

    def test_case_2(self):
        expenditures = [1, 2, 3, 4, 4]
        self.assertEqual(activity_notifications(expenditures, 4), 0)


if __name__ == '__main__':
    unittest.main()
