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

    #Returns list of connections, each connection only featured once though, of course, represented twice in adjacency grid. Func must be expanded to return (i, j, weight: "")
    def traverse_connections(self):
        spots = []
        coord_weights = []
        #prac_grid = [[0,1,2,3], [4,5,6,7], [8,9,10, 11], [12, 13, 14, 15]]
        for j_index, j in enumerate(self.grid):
            #spots += self.grid[j_index][j_index + 1:]
            ls = self.grid[j_index][j_index + 1:]
            coord_weights += [(j_index, j_index + i[0], {"weight": i[1]}) for i in enumerate(ls)]
        return coord_weights

if __name__ == "__main__":
    m = Matrix([1,2,3,4])
    print(m.nodes)
    print(m.grid)
    print(m.traverse_connections())
