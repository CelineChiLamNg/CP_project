import unittest

from parameterized import parameterized

from dnaseq import *


class TestDNA(unittest.TestCase):

    def test_DNAadd(self):
        orig = [1, 2, 3]
        new = 0
        self.assertEqual([1, 2, 3, 0], DNAadd(orig, new))
        self.assertEqual([1, 2, 3], orig)

    def test_DNAprefix(self):
        self.assertEqual([0, 1], DNAprefix([0, 1, 2], 2))
        self.assertEqual([0], DNAprefix([0, 1, 2], 1))
        self.assertEqual([], DNAprefix([0, 1, 2], 0))

    def test_DNAsuffix(self):
        self.assertEqual([1, 2], DNAsuffix([0, 1, 2], 2))
        self.assertEqual([2], DNAsuffix([0, 1, 2], 1))
        self.assertEqual([], DNAsuffix([0, 1, 2], 0))

    @parameterized.expand([
        [True, [1, 2, 3], [1, 2, 3, 0]],
        [True, [1, 2, 3, 0], [1, 2, 3, 0]],
        [True, [1, 2], [1, 2, 3, 0]],
        [False, [2, 2, 3], [1, 2, 3, 0]],
        [True, [], [1, 2, 3, 0]],
        [False, [1, 2, 3, 0, 5], [1, 2, 3, 0]],
        [False, [1, 2, 3, 0], [1, 2, 3]],
        [False, [3, 2, 3], [1, 2, 3, 0]]
    ])
    def test_sequence(self, expected, a, b):
        actual = DNAoccursQ(a, b)
        self.assertEqual(expected, actual)

    def test_DNAoccursQ(self):
        self.assertEqual(False, DNAoccursQ([3, 2, 3], [1, 2, 3, 0]))


    def test_DNAoverlay(self):
        self.assertEqual(7, DNAoverlay([3, 2, 3, 0, 0, 1, 0, 2], [2, 3, 0, 0, 1, 0, 2, 2, 2]))
        self.assertEqual(0, DNAoverlay([], []))
        self.assertEqual(2, DNAoverlay([1, 2, 3], [2, 3, 1]))


if __name__ == '__main__':
    unittest.main()
