import unittest

from graph import *


class TestGraph(unittest.TestCase):

    def test_GRnew(self):
        g = GRnew(4)
        self.assertEqual([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], g)

    def test_GRadd(self):
        g = GRnew(4)

        GRadd(g, 0, 1, 2)

        self.assertEqual([
            [0, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], g)

        GRadd(g, 0, 2, 5)

        self.assertEqual([
            [0, 2, 5, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], g)

    def test_GRadjQ(self):
        g = [[0, 0, 5, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

        self.assertEqual(GRadjQ(g, 0, 0), False)
        self.assertEqual(GRadjQ(g, 3, 1), False)
        self.assertEqual(GRadjQ(g, 0, 2), True)

    def test_GRadj(self):
        g = [[0, 2, 5, 0],
             [0, 0, 0, 0],
             [0, 3, 0, 0],
             [0, 0, 0, 0]]

        self.assertEqual(GRadj(g, 0), [[1, 2], [2, 5]])
        self.assertEqual(GRadj(g, 1), [[], []])
        self.assertEqual(GRadj(g, 2), [[1], [3]])
        self.assertEqual(GRadj(g, 3), [[], []])

    def test_GRindegree(self):
        g = [[0, 2, 5, 0],
             [0, 0, 0, 0],
             [0, 3, 0, 0],
             [0, 0, 0, 0]]

        self.assertEqual(GRindegree(g, 0), 0.0001)
        self.assertEqual(GRindegree(g, 1), 3)
        self.assertEqual(GRindegree(g, 2), 5)
        self.assertEqual(GRindegree(g, 3), 0.0001)

    def test_GRnnodes(self):
        g = [[0, 2, 5, 0],
             [0, 0, 0, 0],
             [0, 3, 0, 0],
             [0, 0, 0, 0]]

        self.assertEqual(GRnnodes(g), 4)
