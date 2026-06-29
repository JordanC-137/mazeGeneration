import itertools
from Matrix import Matrix, ConnectionTuple, Point
import random
from math import sqrt


class term_colors:
    ENDC = "\033[0m"
    GREEN_BACKGROUND = "\033[;42m"
    RED_BACKGROUND = "\033[;41m"
    YELLOW_BACKGROUND = "\033[;103m"
    GREEN_BLOCK = f"{GREEN_BACKGROUND} {ENDC}"
    RED_BLOCK = f"{RED_BACKGROUND} {ENDC}"
    YELLOW_BLOCK = f"{YELLOW_BACKGROUND} {ENDC}"
    
# Create fully connected 'lattice' for maze
def create_maze(n):
    nodes = list(itertools.product(range(n), repeat = 2))
    m = Matrix(nodes)
    #Make horizontal connections
    for j in range(n): 
        for i in range(n - 1):
            m.add_connection((i, j), (i+1, j))

    #Make vertical connections
    for i in range(n):
        for j in range(n-1):
            m.add_connection((i, j), (i, j+1))
    return m
    
def create_maze_new(n):
    nodes = list(itertools.product(range(n), repeat = 2))
    maze = Matrix(nodes)
    for j in range(n): 
        for i in range(n - 1):
            maze.add_connection_new(Point((i, j)), Point((i+1, j)))

    #Make vertical connections
    for i in range(n):
        for j in range(n-1):
            maze.add_connection_new(Point((i, j)), Point((i, j+1)))
    return maze

# Find and remove smallest connection
def pop_minimum_connection(s1, s2, ls):
    filtered = [i for i in ls if i.x in s1 and i.y in s2] + [i for i in ls if i.x in s2 and i.y in s1]
    min_connection = min(filtered, key = lambda x: x.weight)
    ls.remove(min_connection)
    return (min_connection,ls)

# Expect ls to be a set
def pop_minimum_connection_new(set1, set2, ls):
    connections_spanning_sets = {connection for connection in ls if connection.has_value_in_each_set(set1, set2)}
    min_connection = min(connections_spanning_sets, key=lambda x: x.weight)
    connections_spanning_sets.remove(min_connection)
    return(min_connection, connections_spanning_sets)

def cross_set_connections(s1, s2, ls):
    l1 = {i for i in ls if i.x in s1 and i.y in s2}
    #Twist x, y order for l2 so that maintained consistency for u in s1 and v in s2
    l2 = {ConnectionTuple(i.y, i.x, i.weight) for i in ls if i.x in s2 and i.y in s1}
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

def get_euclidean_distance(a, b):
    diff_in_y = b[1] - a[1]
    diff_in_x = b[0] - a[0]
    return sqrt(diff_in_x ** 2 + diff_in_y ** 2)

def get_euclidean_distance_new(point1, point2):
    diff_in_y = point1.y - point2.y
    diff_in_x = point1.x - point2.x
    return sqrt(diff_in_x ** 2 + diff_in_y ** 2)

# If minimum_distance, only accept start and endpoints with a euclidean distance greater than that value
def get_start_and_endpoints(maze, minimum_distance):
    start_point, end_point = random.sample(maze.nodes, 2)
    if minimum_distance is None:
        return [start_point, end_point]
    else:
        while(get_euclidean_distance(start_point, end_point) < minimum_distance):
            start_point, end_point = random.sample(maze.nodes, 2)
    return [start_point, end_point]


def get_start_and_end_new(maze, minimum_distance):
    start_point, end_point = random.sample(maze.nodes, 2)
    if minimum_distance is None:
        return [start_point, end_point]
    else:
        while(get_euclidean_distance_new(start_point, end_point) < minimum_distance):
            start_point, end_point = random.sample(maze.nodes, 2)
    return [start_point, end_point]

# Create and output maze
def print_maze(m, conns, dimensions):
    conns_set = [set(i) for i in conns]
    start_point, end_point = get_start_and_endpoints(m, 10)

    border = ' ' * (dimensions * 2 + 1)
    print(f"{term_colors.RED_BACKGROUND}{border}{term_colors.ENDC}")

    for j in range(dimensions):
        #Build horizontal row consisting of nodes and horizontal connections
        row = term_colors.RED_BLOCK
        for i in range(dimensions):
            current_point = (i, j)
            if current_point == start_point or current_point == end_point:
                block = term_colors.YELLOW_BLOCK
            else:
                block = term_colors.GREEN_BLOCK
            # Confirm that connection to right of current block, is clear/not a wall
            if set((current_point, (i + 1, j))) in conns_set:
                row += f"{block}{term_colors.GREEN_BLOCK}"

            else:
                row += f"{block}{term_colors.RED_BLOCK}"
        print(f"{row}")
        
        #Sub-loop for representing south connection for each co-ordinate
        row = term_colors.RED_BLOCK
        for i in range(dimensions):
            if set(((i, j), (i, j + 1))) in conns_set:
                row += f"{term_colors.GREEN_BLOCK}{term_colors.RED_BLOCK}"
            else:
                row += term_colors.RED_BLOCK * 2
        print(f"{row}")



if __name__ == "__main__":
    n = 20
    m = create_maze(n)
    ls = mst(m)
    print_maze(m, ls, n)