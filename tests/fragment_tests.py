import unittest

from fraglist import *


class TestFragments(unittest.TestCase):

    def test_should_return_empty_list_for_empty_list(self):
        l = []
        purged = FLpurge(l)

        self.assertEqual([], purged)

    def test_should_return_one_element_if_list_is_one_element(self):
        l = [[1, 2, 3]]
        purged = FLpurge(l)

        self.assertEqual([[1, 2, 3]], purged)

    def test_first_tests(self):
        l = [[1, 2, 3, 0], [1, 2, 3]]
        purged = FLpurge(l)

        self.assertEqual([[1, 2, 3, 0]], purged)

    def test_first_tests2(self):
        l = [[1, 2, 3], [1, 2, 3, 0]]
        purged = FLpurge(l)

        self.assertEqual([[1, 2, 3, 0]], purged)

    def test_second(self):
        l = [[1, 2, 3, 0], [1, 2, 3], [1, 2]]
        purged = FLpurge(l)

        self.assertEqual([[1, 2, 3, 0]], purged)

    def test_third(self):
        l = [[1, 2, 3, 0], [1, 2, 3, 0], [1, 2], [3, 2, 3]]
        print(FLpurge([[1, 2, 3, 0], [1, 2, 3, 0], [1, 2], [3, 2, 3]]))

        purged = FLpurge(l)

        self.assertEqual([[1, 2, 3, 0], [3, 2, 3]], purged)

    def test_FLpurge_bug1(self):
        l = [[1, 3], [3, 2, 2, 1], [2, 1], [2, 1], [3, 2, 2, 1, 3, 1], [3, 3, 2, 2, 1], [1, 3, 1],
             [1, 3, 3, 2, 2, 1, 3, 1],
             [1, 3, 3, 2], [2, 2, 1, 3, 1], [0, 1, 3], [2, 1, 3, 1], [2, 1, 3, 1], [3, 2, 2, 1, 3, 1],
             [3, 0, 1, 3, 3, 2]]

        expected = [
            [1, 3, 3, 2, 2, 1, 3, 1],
            [3, 0, 1, 3, 3, 2]]
        purged = FLpurge(l)
        self.assertEqual(expected, purged)

    def test_Fladd(self):
        self.assertEqual(
            [[2, 1, 0], [0, 1, 2], [2, 1, 0]],
            Fladd(
                [[2, 1, 0], [0, 1, 2]],
                [2, 1, 0],
            ))

    def test_FLpos(self):
        self.assertEqual(
            [2, 1, 0],
            FLpos(
                [[2, 1, 0], [0, 1, 2], [2, 1, 0]],
                0
            ))


if __name__ == '__main__':
    unittest.main()
