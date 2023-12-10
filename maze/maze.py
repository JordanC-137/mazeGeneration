import itertools
from Matrix import Matrix, Connection
import random


class term_colors:
    ENDC = "\033[0m"
    GREEN_BACKGROUND = "\033[;42m"
    RED_BACKGROUND = "\033[;41m"
    YELLOW_BACKGROUND = "\033[;103m"
    GREEN_BLOCK = f"{GREEN_BACKGROUND} {ENDC}"
    RED_BLOCK = f"{RED_BACKGROUND} {ENDC}"
    YELLOW_BLOCK = f"{YELLOW_BACKGROUND} {ENDC}"
    

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

#TODO: Include euclidean distance clause for start/end point selection
def print_maze(m, conns, dimensions):
    conns_set = [set(i) for i in conns]
    border = ' ' * (dimensions * 2 + 1)

    start_point, end_point = random.sample(m.nodes, 2)
    print(f"Start: {start_point}    End: {end_point}")
    print(f"{term_colors.RED_BACKGROUND}{border}{term_colors.ENDC}")

    for j in range(dimensions):
        #Build horizontal row consisting of nodes and horizontal connections
        row = term_colors.RED_BLOCK
        for i in range(dimensions):

            #Pick Yellow or Green whether co-ordinate is a start/end point or not
            if (j, i) == start_point or (j, i) == end_point:
                block = term_colors.YELLOW_BLOCK
            else:
                block = term_colors.GREEN_BLOCK
            if set(((j, i), (j, i + 1))) in conns_set:
                #row += term_colors.GREEN_BLOCK * 2
                row += f"{block}{term_colors.GREEN_BLOCK}"

            else:
                #row += f"{term_colors.GREEN_BLOCK}{term_colors.RED_BLOCK}"
                row += f"{block}{term_colors.RED_BLOCK}"
        print(f"{row}")
        
        #Sub-loop for representing south connection for each co-ordinate
        row = term_colors.RED_BLOCK
        for i in range(dimensions):
            if set(((j, i), (j + 1, i))) in conns_set:
                row += f"{term_colors.GREEN_BLOCK}{term_colors.RED_BLOCK}"
            else:
                row += term_colors.RED_BLOCK * 2
        print(f"{row}")



if __name__ == "__main__":
    m = create_maze(20)
    ls = mst(m)
    print_maze(m, ls, 20)