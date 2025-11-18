import unittest
from src.homework.g_lists_and_tuples.lists import get_p_distance, get_p_distance_matrix


class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        a = ['T','T','T','C','C','A','T','T','T','A']
        b = ['G','A','T','T','C','A','T','T','T','C']
        self.assertAlmostEqual(get_p_distance(a, b), 0.4, places=3)

    def test_get_p_distance_matrix(self):
        seqs = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A'],
        ]

        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0],
        ]

        mat = get_p_distance_matrix(seqs)
        self.assertEqual(len(mat), len(expected))
        for i in range(len(expected)):
            for j in range(len(expected)):
                self.assertAlmostEqual(mat[i][j], expected[i][j], places=3)


if __name__ == '__main__':
    unittest.main()
