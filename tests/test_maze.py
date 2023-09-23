import unittest
import sys
sys.path.append("../maze")
from Matrix import Matrix, Connection

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
        

if __name__ == '__main__':
    unittest.main()