import unittest

from SangueSuorEMuitasLagrimass import *
from unittest import *


class TestAlgo(TestCase):

    def test_grafo_pesos(self):
        zero = [2, 0, 1, 3, 0]
        one = [0, 1, 1, 1]
        two = [1, 2, 0, 0, 0, 3]
        three = [3, 0, 1, 0]

        g = grafo_pesos([zero, one, two, three])
        expected_graph = [[0, 1, 0, 2],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1],
                          [0, 1, 0, 0]]
        self.assertEqual(expected_graph, g)

    def test_pesos_no_inicial(self):
        g = [[0, 1, 0, 2],
             [0, 0, 1, 0],
             [0, 0, 0, 1],
             [0, 1, 0, 0]]

        self.assertEqual([0.0001, 1, 1, 2], pesos_no_inicial(g))

    def test_algorithm(self):
        expected_answer = [3, 0, 1, 3, 3, 2, 2, 1, 3, 1]
        raw_fragments = [[1, 3], [3, 2, 2, 1], [2, 1], [2, 1], [3, 2, 2, 1, 3, 1], [3, 3, 2, 2, 1], [1, 3, 1],
                         [1, 3, 3, 2, 2, 1, 3, 1],
                         [1, 3, 3, 2], [2, 2, 1, 3, 1], [0, 1, 3], [2, 1, 3, 1], [2, 1, 3, 1], [3, 2, 2, 1, 3, 1],
                         [3, 0, 1, 3, 3, 2]]

        self.assertEqual(expected_answer, algoritmo(raw_fragments, 100))


    def test_algorithm(self):
        expected_answer = [3, 0, 1, 3, 3, 2, 2, 1, 3, 1]
        raw_fragments = [[1, 3], [3, 2, 2, 1], [2, 1], [2, 1], [3, 2, 2, 1, 3, 1], [3, 3, 2, 2, 1], [1, 3, 1],
                         [1, 3, 3, 2, 2, 1, 3, 1],
                         [1, 3, 3, 2], [2, 2, 1, 3, 1], [0, 1, 3], [2, 1, 3, 1], [2, 1, 3, 1], [3, 2, 2, 1, 3, 1],
                         [3, 0, 1, 3, 3, 2]]

        self.assertEqual(expected_answer, algoritmo(raw_fragments, 100))

    def test_algoritmo_from_the_pdf(self):
        zero = [2, 0, 1, 3, 0]
        one = [0, 1, 1, 1]
        two = [1, 2, 0, 0, 0, 3]
        three = [3, 0, 1, 0]

        fragments = [zero, one, two, three]
        expected_graph = [[0, 1, 0, 2],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1],
                          [0, 1, 0, 0]]

        expected_answer = [2, 0, 1, 3, 0, 1, 0, 1, 1, 1, 2, 0, 0, 0, 3]

        self.assertEqual(expected_answer, algoritmo(fragments, 3))

    def test_algo_using_randomness(self):
        [original, fragments] = utils.generate_and_return_original_and_fragments(1000, 80, 20, 25)

        print('original =', original)
        print('fragments =', fragments)
        self.assertEqual(original, algoritmo(fragments, 1000))

    def test_bug1(self):
        original = [0, 1, 2, 0, 1, 2, 3, 2, 1, 0]
        fragments = [[0, 1, 2], [2, 0, 1, 2, 3, 2], [1, 2, 3, 2, 1, 0], [0, 1], [2, 0, 1, 2, 3, 2],
                     [0, 1, 2, 0, 1, 2, 3, 2, 1, 0]]

        self.assertEqual(original, algoritmo(fragments, 3000))

    def test_bug2(self):

        original = [3, 2, 3, 0, 0, 1, 0, 2, 2, 2]
        fragments = [[1, 0, 2, 2, 2], [3, 0, 0, 1], [2, 2, 2], [0, 2, 2, 2], [3, 0, 0, 1, 0, 2, 2, 2], [2, 3, 0],
                     [0, 1, 0, 2, 2, 2], [0, 2, 2], [0, 0, 1, 0, 2, 2], [3, 0, 0, 1, 0, 2, 2, 2], [0, 1, 0, 2, 2, 2],
                     [0, 1, 0, 2, 2], [0, 2, 2, 2], [1, 0, 2, 2, 2], [3, 0, 0, 1], [0, 2, 2, 2], [2, 2, 2],
                     [2, 3, 0, 0, 1, 0, 2, 2, 2], [0, 1, 0, 2, 2, 2], [1, 0, 2], [2, 3, 0, 0, 1, 0, 2, 2], [2, 2, 2],
                     [0, 0, 1, 0, 2, 2], [0, 0, 1, 0, 2, 2, 2], [0, 0], [0, 1, 0, 2], [3, 2, 3, 0, 0, 1, 0, 2]]

        self.assertEqual(original, algoritmo(fragments, 3000, original))

    def test_bug3(self):

        original = [1, 1, 1, 1, 0, 0, 3, 0, 2, 1]
        fragments = [[0, 0, 3, 0, 2, 1], [1, 1], [3, 0, 2, 1], [3, 0, 2, 1], [0, 3, 0, 2, 1], [0, 2, 1],
                     [1, 1, 1, 0, 0, 3]]

        self.assertEqual(original, algoritmo(fragments, 3000, original))

    def test_find_the_first_node(self):
        zero = [2, 0, 1, 3, 0]
        one = [0, 1, 1, 1]
        two = [1, 2, 0, 0, 0, 3]
        three = [3, 0, 1, 0]

        fragments = [zero, one, two, three]
        g = [[0, 1, 0, 2],
             [0, 0, 1, 0],
             [0, 0, 0, 1],
             [0, 1, 0, 0]]

        dna = [2, 0, 1, 3, 0, 1, 0, 1, 1, 1, 2, 0, 0, 0, 3]

        for i in range(100):
            self.assertGreaterEqual(encontrar_primeiro_no(g), 0)
            self.assertLessEqual(encontrar_primeiro_no(g), 3)

    def test_find_next_node(self):
        zero = [2, 0, 1, 3, 0]
        one = [0, 1, 1, 1]
        two = [1, 2, 0, 0, 0, 3]
        three = [3, 0, 1, 0]

        fragments = [zero, one, two, three]
        g = [[0, 1, 0, 2],
             [0, 0, 1, 0],
             [0, 0, 0, 1],
             [0, 1, 0, 0]]

        dna = [2, 0, 1, 3, 0, 1, 0, 1, 1, 1, 2, 0, 0, 0, 3]

        for i in range(100):
            self.assertGreaterEqual(encontrar_proximo_no(g, [0]), 0)
            self.assertLessEqual(encontrar_proximo_no(g, [0]), 3)

            # TODO check this
            # self.assertNotEqual(find_next_node(g, [0]), 0)


if __name__ == '__main__':
    unittest.main()
