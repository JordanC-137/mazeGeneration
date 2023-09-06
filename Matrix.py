import itertools
import random

print("Hello World")


class Matrix:
    def __init__(self):
        self.nodes = list(itertools.product([0,1,2], repeat = 2))
        self.grid = [[None for i in range(len(self.nodes))] for i in range(len(self.nodes))]
        print(self.nodes)
        self.display_grid()

    def display_grid(self):
        [print(i) for i in self.grid]
    
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
        self.display_grid()

m = Matrix()
print()
m.add_connection((0,0), (0,1), 5)
m.add_connection((1,2), (2,2))