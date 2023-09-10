"""from maze import Matrix

from Matrix import Matrix """
import unittest
from maze.Matrix import Matrix

class TestMod(unittest.TestCase):
    def test_module(self):
        m = Matrix()
        self.assertEqual(m.nodes, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])

if __name__ == '__main__':
    unittest.main()