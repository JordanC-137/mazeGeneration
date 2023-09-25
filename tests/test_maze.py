import unittest
import sys
sys.path.append("../maze")
from Matrix import Matrix, Connection
from maze import cross_set_connections

class TestMaze(unittest.TestCase):
    def test_maze1_nodes_and_edges(self):
        m = Matrix([1,2,3,4])
        node_bool = ([1, 2, 3, 4], m.nodes)
        grid_bool = (m.grid, [[None, None, None, None] for i in range(4)])
        self.assertTrue(node_bool and grid_bool)

    def test_maze_applied_connections(self):
        m = Matrix([1,2,3,4])
        m.add_connection(1, 2, 5)
        m.add_connection(2, 3, 6)
        m.add_connection(4, 3, 7)
        m.add_connection(1, 4, 8)
        traversed_connections = [i.weight for i in m.traverse_connections()]
        self.assertEqual(traversed_connections,[5, None, 8, 6, None, 7])
    
    def test_cross_set_connection_function(self):
        s1 = [1,3,5]
        s2 = [2]
        vals = [(1,2), (2, 3), (5,5)]
        vals = [Connection(i[0], i[1], 0) for i in vals]
        ls = cross_set_connections(s1, s2, vals)
        ls = [(i.x, i.y) for i in ls]
        self.assertEqual(ls, [(1, 2), (3, 2)])
    
    def test_mst(self):
        m = Matrix([0, 1, 2, 3, 4])
        m.add_connection(0,1,8)
        m.add_connection(2,0,5)
        m.add_connection(2,1,9)
        m.add_connection(3,1,11)
        m.add_connection(2,4,10)
        m.add_connection(2,3,15)
        m.add_connection(3,4,7)
        

if __name__ == '__main__':
    unittest.main()