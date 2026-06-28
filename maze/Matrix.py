import itertools
import random
from collections import namedtuple

ConnectionTuple = namedtuple("Connection", "x y weight")

class Matrix:
    def __init__(self, nodes = None):
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = list(itertools.product([0,1,2], repeat = 2))
        self.grid = [[None for i in range(len(self.nodes))] for i in range(len(self.nodes))]

    def display_grid(self):
        [print(i) for i in self.grid]
        
    def get_element(self, index):
        return self.nodes[index]
    
    def add_connection(self, node1, node2, weight = None):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise IndexError("One of these nodes is not in the grid")
        pos1 = self.nodes.index(node1)
        pos2 = self.nodes.index(node2)
        if weight:
            self.grid[pos1][pos2] = weight
            self.grid[pos2][pos1] = weight
        else:
            random_value = random.randint(0,20)
            self.grid[pos1][pos2] = random_value
            self.grid[pos2][pos1] = random_value

    def remove_connection(self, node1, node2):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise IndexError("One of these nodes is not in the grid")
        pos1 = self.nodes.index(node1)
        pos2 = self.nodes.index(node2)
        self.grid[pos1][pos2] = None
        self.grid[pos2][pos1] = None

    def traverse_connections(self):
        coordinate_weights = []
        for j_index in range(len(self.grid)):
            ls = self.grid[j_index][j_index + 1:]
            coordinate_weights += [ConnectionTuple(self.get_element(j_index), self.get_element(j_index + i[0] + 1), i[1]) for i in enumerate(ls)]
        #Filter out non-connections
        coordinate_weights = [i for i in coordinate_weights if i.weight]
        return coordinate_weights

if __name__ == "__main__":
    m = Matrix([1,2,3,4])
    m.display_grid()
    m.add_connection(1,3,5)
    ls = m.traverse_connections()
    print(ls)
