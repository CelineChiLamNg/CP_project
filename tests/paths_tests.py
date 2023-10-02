import unittest

from dnapaths import *


class TestPaths(unittest.TestCase):
    def test_Pnew(self):
        g = [[0, 2, 5, 0],
             [0, 0, 0, 0],
             [0, 3, 0, 0],
             [0, 0, 0, 0]]

        self.assertEqual(Pnew(g, 0), [0])
        self.assertEqual(Pnew(g, 1), [1])
        self.assertEqual(Pnew(g, 2), [2])
        self.assertEqual(Pnew(g, 3), [3])

    def test_Padd(self):
        g = [[0, 2, 5, 0],
             [0, 0, 0, 1],
             [0, 3, 0, 0],
             [0, 0, 0, 0]]

        c = [0, 1]

        Padd(g, c, 3)

        self.assertEqual([0, 1, 3], c)

    def test_Ploop(self):
        g = [[0, 2, 5, 0],
             [0, 0, 0, 1],
             [0, 3, 0, 0],
             [0, 1, 0, 0]]

        c = [0, 2, 1, 3]

        self.assertEqual(Ploop(g, c), False)

        g = [[0, 2, 5, 0],
             [0, 0, 0, 1],
             [0, 3, 0, 0],
             [0, 1, 0, 0]]

        c = [0, 2, 1, 3, 0]

        self.assertEqual(Ploop(g, c), True)

        g = [[0, 2, 5, 0],
             [0, 0, 0, 1],
             [0, 3, 0, 0],
             [0, 1, 0, 0]]

        c = [0, 2, 1, 3, 2]

        # TODO: maybe this should be True if our understanding of what a cycle is changes
        # self.assertEqual(Ploop(g, c), False)

    def test_PHamiltonianQ(self):
        g = [[0, 2, 5, 0],
             [0, 0, 0, 1],
             [0, 3, 0, 0],
             [0, 1, 0, 0]]

        self.assertEqual(PHamiltonianQ(g, [0, 2, 1, 3]), True)
        self.assertEqual(PHamiltonianQ(g, [2, 1, 3, 0]), True)
        self.assertEqual(PHamiltonianQ(g, [1, 3, 0, 2]), True)
        self.assertEqual(PHamiltonianQ(g, [3, 0, 2, 1]), True)

        self.assertEqual(PHamiltonianQ(g, []), False)
        self.assertEqual(PHamiltonianQ(g, [0, 2, 1]), False)
        self.assertEqual(PHamiltonianQ(g, [0, 2, 1, 2]), False)
        self.assertEqual(PHamiltonianQ(g, [0, 2, 1, 0]), False)
        self.assertEqual(PHamiltonianQ(g, [0, 2, 1, 0, 2]), False)

        # TODO maybe cover this case
        # self.assertEqual(PHamiltonianQ(g, [3, 1, 2, 0]), False)

    def test_PextendableQ(self):
        g = [[0, 3, 5, 1],
             [2, 0, 1, 1],
             [4, 3, 0, 1],
             [1, 1, 2, 0]]

        self.assertEqual(PextendableQ(g, [0, 1, 0]), True)
        self.assertEqual(PextendableQ(g, [0, 2]), True)
        self.assertEqual(PextendableQ(g, [0]), True)

        self.assertEqual(PextendableQ(g, [0, 2, 1, 3]), False)
        self.assertEqual(PextendableQ(g, [2, 1, 3, 0]), False)
        self.assertEqual(PextendableQ(g, [1, 3, 0, 2]), False)
        self.assertEqual(PextendableQ(g, [3, 0, 2, 1]), False)

    def test_Pextendable_bug1(self):
        graph = [[0, 1, 0, 2], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]]

        p = [0]
        PextendableQ(graph, p)
        self.assertEqual(p, [0])

    def test_Pseq(self):
        zero = [2, 0, 1, 3, 0]
        one = [0, 1, 1, 1]
        two = [1, 2, 0, 0, 0, 3]
        three = [3, 0, 1, 0]

        fragments = [zero, one, two, three]
        g = [[0, 1, 0, 2],
             [0, 0, 1, 0],
             [0, 0, 0, 1],
             [0, 1, 0, 0]]

        expected_dna = [2, 0, 1, 3, 0, 1, 0, 1, 1, 1, 2, 0, 0, 0, 3]

        discovered_path = [0, 3, 1, 2]
        calculated_dna = Pseq(g, discovered_path, fragments)

        self.assertEqual(expected_dna, calculated_dna)

    def test_Pseq_bug1(self):
        grafo = [[0, 0], [1, 0]]

        purged = [[2, 3, 0, 0, 1, 0, 2, 2, 2], [3, 2, 3, 0, 0, 1, 0, 2]]

        p = [1, 0]

        actual = Pseq(grafo, p, purged)

        self.assertEqual([3, 2, 3, 0, 0, 1, 0, 2, 2, 2], actual)


if __name__ == '__main__':
    unittest.main()
