import unittest
import sys
sys.path.append("../maze")
from Matrix import Matrix, Connection
from maze import cross_set_connections

class TestMST1(unittest.TestCase):
    def test_mst1_edges(self):
        m = Matrix([0, 1, 2, 3, 4])
        m.add_connection(0,1,8)
        m.add_connection(2,0,5)
        m.add_connection(2,1,9)
        m.add_connection(3,1,11)
        m.add_connection(2,4,10)
        m.add_connection(2,3,15)
        m.add_connection(3,4,7)

        expect = [Connection(0,1,8)]
        expect.append(Connection(0, 2, 5))
        expect.append(Connection(1, 2, 9))
        expect.append(Connection(1, 3, 11))
        expect.append(Connection(2, 3, 15))
        expect.append(Connection(2, 4, 10))
        expect.append(Connection(3, 4, 7))
        self.assertEqual(m.traverse_connections(), expect)

if __name__ == '__main__':
    unittest.main()