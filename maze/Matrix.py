import itertools
import random


class Matrix:
    def __init__(self, nodes = None):
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = list(itertools.product([0,1,2], repeat = 2))
        self.grid = [[None for i in range(len(self.nodes))] for i in range(len(self.nodes))]

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

    def remove_connection(self, node1, node2):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise IndexError("One of these nodes is not in the grid")
        pos1 = self.nodes.index(node1)
        pos2 = self.nodes.index(node2)
        self.grid[pos1][pos2] = None
        self.grid[pos2][pos1] = None

    #Traverse grid, not crossing i=j diagonal
    def traverse_connections(self):
        spots = []
        #prac_grid = [[0,1,2,3], [4,5,6,7], [8,9,10, 11], [12, 13, 14, 15]]
        for j_index, j in enumerate(self.grid):
            spots += self.grid[j_index][j_index + 1:]
        return spots

if __name__ == "__main__":
    m = Matrix([[0,1,2,3], [4,5,6,7], [8,9,10, 11], [12, 13, 14, 15]])
    print(m.nodes)
    print(m.traverse_connections())
