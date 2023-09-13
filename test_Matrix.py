
import unittest
from maze.Matrix import Matrix

class TestMod(unittest.TestCase):
    def test_initialisation(self):
        m = Matrix()
        self.assertEqual(m.nodes, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
    
    def test_connections(self):
        m = Matrix([1,2,3,4])
        m.add_connection(1, 3, 5)
        expect = [None, 5, None, None, None, None]
        self.assertEqual(m.traverse_connections(), expect)

if __name__ == '__main__':
    unittest.main()