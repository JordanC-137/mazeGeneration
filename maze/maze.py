import itertools
from Matrix import Matrix, Connection
import random

#TODO: delete span_tree branch
class term_colors:
    GREEN_FOREGROUND = "\033[92m"
    ENDC = "\033[0m"
    GREEN_BACKGROUND = "\033[;42m"
    RED_BACKGROUND = "\033[;41m"
    GREEN_BLOCK = f"{GREEN_BACKGROUND} {ENDC}"
    RED_BLOCK = f"{RED_BACKGROUND} {ENDC}"

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

#Returns list of co-ord tuples E.g. [(0, 1), (0,2)]
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

def print_maze(m, conns, dimensions):
    #connections = [set([i.x, i.y]) for i in m.traverse_connections()]
    #conns = [((0, 0), (1, 0))]
    conns = [set(i) for i in conns]
    border = 'w' * (dimensions * 2 + 1)

    start_point, end_point = random.sample(m.nodes, 2)

    print(border)
    for j in range(dimensions):
        #Build horizontal row consisting of nodes and horizontal connections
        row = "w"
        for i in range(dimensions):
            if set(((j, i), (j, i + 1))) in conns:
                row += "  "
            else:
                row += " w"
        print(f"{row}")

        row = "w"
        for i in range(dimensions):
            if set(((j, i), (j + 1, i))) in conns:
                row += " w"
            else:
                row += "ww"
        print(f"{row}")



if __name__ == "__main__":
    m = create_maze(3)
    ls = mst(m)
    print(ls)
    print_maze(m, ls, 3)