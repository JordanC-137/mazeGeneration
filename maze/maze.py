import itertools
from Matrix import Matrix, Connection

#TODO: delete span_tree branch

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
    m.add_connection((2,1), (2,2))

def create_maze(n):
    nodes = list(itertools.product(range(n), repeat = 2))
    m = Matrix(nodes)

    #Make horizontal connections
    for j in range(n): 
        for i in range(n - 1):
            m.add_connection((j, i), (j, i+1))

    #Make vertical connections
    for i in range(n):
        for j in range(n-1):
            m.add_connection((j, i), (j + 1, i))
    return m
    

def pop_minimum_connection(s1, s2, ls):
    filtered = [i for i in ls if i.x in s1 and i.y in s2] + [i for i in ls if i.x in s2 and i.y in s1]
    min_connection = min(filtered, key = lambda x: x.weight)
    ls.remove(min_connection)
    return (min_connection,ls)

def cross_set_connections(s1, s2, ls):
    l1 = {i for i in ls if i.x in s1 and i.y in s2}
    #Twist x, y order for l2 so that maintained consistency for u in s1 and v in s2
    l2 = {Connection(i.y, i.x, i.weight) for i in ls if i.x in s2 and i.y in s1}
    l1.update(l2)
    return l1

def mst(m):
    s1 = [m.nodes[0]]
    s2 = m.nodes[1:]
    T = []
    edges = m.traverse_connections()
    E = cross_set_connections(s1, s2, edges)
    while s2:
        min_edge, E_removed_minimum = pop_minimum_connection(s1, s2, E)
        E = E_removed_minimum
        T.append((min_edge.x, min_edge.y))
        v = min_edge[1]
        s2.remove(v)
        s1.append(v)
        E.update(cross_set_connections(s1, s2, edges))
    return T

def print_maze(m, dimensions):
    connections = [(i.x, i.y) for i in m.traverse_connections()]

    border = f"+{'w' * (2 * dimensions - 1)}+"
    print(border)
    for j in range(dimensions - 1):
        row = ""
        path = True
        if path:
            row += "w"
            for i in range(dimensions):
                if ((i, j), (i+1, j)) in connections:
                    row += " "
                else:
                    row += "w"
                row += "w"
            path = False
        else:
            row += "w"
            for i in range(dimensions):
                if((i, j), (i, j+ 1)) in connections:
                    row += " "
                else:
                    row += "w"
                row += "w"
            path = False
        print(row)
    print(border)
                
            


    """
    for j in range(dimensions):
        for i in range(dimensions):
    """


if __name__ == "__main__":
    m = create_maze(3)
    print_maze(m, 3)