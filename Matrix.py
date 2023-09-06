import itertools
import random

print("Hello World")


class Matrix():
    def __init__(self):
        self.nodes = list(itertools.product([0,1,2], repeat = 2))
        self.grid = [[None for i in range(len(self.nodes))] for i in range(len(self.nodes))]
        print(self.nodes)
        print(self.grid)

    def add_connection(self, node1, node2,weight = None):
        pos1 = self.nodes.index(node1)
        pos2 = self.nodes.index(node2)
        if weight:
            self.grid[pos1][pos2] = weight
            self.grid[pos1][pos2] = weight
        print(self.grid)

m = Matrix()
m.add_connection((0,0), (0,1), 5)