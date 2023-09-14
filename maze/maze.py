from Matrix import Matrix


def build_maze(m):
    m.add_connection((0,0), (0,1))
    m.add_connection((0,1), (0,2))
    m.add_connection((1,0), (0,0))
    m.add_connection((0,1), (1,1))
    m.add_connection((0,2), (1,2))
    m.add_connection((1,0), (1,1))
    m.add_connection((1,1), (1,2))
    m.add_connection((1,1), (2,1))
    m.add_connection((2,2), (1,2))
    m.add_connection((2,0), (2,1))
    m.add_connection((2,0), (1,0))
    m.add_connection((2,0), (2,1))
    m.add_connection((2,1), (2,2))
    

m = Matrix([1,2,3,4])
print(m.nodes)