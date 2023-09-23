import unittest
import sys
sys.path.append("../maze")
from Matrix import Matrix, Connection

class TestMod(unittest.TestCase):
    def test_initial_nodes(self):
        m = Matrix()
        self.assertEqual(m.nodes, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
    
    def test_initial_grid(self):
        m = Matrix()
        ls = [[None for i in range(9)] for j in range(9)]
        self.assertEqual(m.grid, ls)

    def test_add_connection(self):
        m = Matrix([1,2,3,4])
        m.add_connection(2,3,4)
        m.add_connection(4, 1, 10)
        ls = [[None, None, None, 10],[None, None, 4, None],[None, 4, None, None],[10, None, None, None]]
        self.assertEqual(m.grid, ls)

    def test_traverse_connections(self):
        m = Matrix([1,2,3,4])
        m.add_connection(1, 3, 5)
        expect = [Connection(0, 0, None), Connection(0, 1, 5), Connection(0, 2, None), Connection(1, 1, None), Connection(1, 2, None), Connection(2, 2, None)]
        self.assertEqual(m.traverse_connections(), expect)

if __name__ == '__main__':
    unittest.main()