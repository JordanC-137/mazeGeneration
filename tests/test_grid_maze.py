import unittest
import sys
sys.path.append("../maze")
from Matrix import Matrix, Connection
from maze import cross_set_connections, mst

class TestGridMST(unittest.TestCase):
    def test_mst1(self):
        m = Matrix([(0, 0),(0, 1), (1, 0), (1, 1)])
        m.add_connection((0, 0), (0, 1), 2)
        m.add_connection((0, 0), (1, 0), 10)
        m.add_connection((0, 1), (1, 1), 5)
        m.add_connection((1, 0), (1, 1), 7)

        T = mst(m)
        self.assertEqual(T, [((0, 0), (0, 1)), ((0, 1), (1, 1)), ((1, 1), (1, 0))])
    

if __name__ == '__main__':
    unittest.main()