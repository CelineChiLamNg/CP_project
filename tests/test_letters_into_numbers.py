import unittest

from letters_into_numbers import *


class TestTurnLettersIntoNumbers(unittest.TestCase):

    def test_grafo_pesos(self):
        self.assertEqual([0], ofDNA('A'))
        self.assertEqual([1], ofDNA('C'))
        self.assertEqual([2], ofDNA('T'))
        self.assertEqual([3], ofDNA('G'))
        self.assertEqual([2, 2, 2], ofDNA('TTT'))
        self.assertEqual([0, 1, 2, 3], ofDNA('ACTG'))

        print(ofDNA('TACGA'))
        print(ofDNA('ACCC'))
        print(ofDNA('CTAAAG'))
        print(ofDNA('GACA'))
        print(ofDNA('TACGACACCCTAAAG'))


if __name__ == '__main__':
    unittest.main()
