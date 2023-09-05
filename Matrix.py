import itertools

print("Hello World")


class Matrix():
    def __init__(self):
        self.grid = [[None for i in range(3)] for i in range(3)]
        self.nodes = list(itertools.product([0,1,2], repeat = 2))

    def add_connection(self,weight = None):
        pass

m = Matrix()
print(m.nodes)
#print(m.grid)