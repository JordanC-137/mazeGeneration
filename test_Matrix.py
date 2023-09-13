
import unittest
from maze.Matrix import Matrix

class TestMod(unittest.TestCase):
    def test_initialisation(self):
        m = Matrix()
        self.assertEqual(m.nodes, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
    
    def test_connections(self):
        m = Matrix()
        m.add_connection((0,2), (0,1), 1)
        self.assertEqual(m.traverse_connections(), [[1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]])

if __name__ == '__main__':
    unittest.main()