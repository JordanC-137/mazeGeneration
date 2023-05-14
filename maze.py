import networkx as nx
import matplotlib.pyplot as plt
import random

#https://www.baeldung.com/cs/maze-generation
# TODO export lattice object to seperate Maze class with attributes such as start and end point

L = 3
lattice = nx.grid_2d_graph(L,L)

#Node and eges of baeldung graph
def _testgraph():
    test_graph_edges = [(0, 1, 8), (0, 2, 5), (1,3, 11), (1, 2, 9)]
    test_graph_edges = map(lambda x: (x[0], x[1], {"weight": x[2]}), test_graph_edges)
    test_graph = nx.Graph()
    test_graph.add_edges_from(test_graph_edges)
    return test_graph

def get_nodes():
    return list(lattice)

def get_edges():
    return list(lattice.edges)

def assign_random_edges():
    for source, destination in lattice.edges():
        lattice[source][destination]['weight'] = random.randint(0, 100)

def draw_graph(route):
    nx.draw(lattice)
    plt.savefig(route)

def minSpanningTree():
    nodes = get_nodes()
    arbit_node = random.choice(nodes)
    s1 = [arbit_node]
    s2 = [i for i in nodes if i is not arbit_node]

    edges = get_edges()
    #T can be a set, to prevent duplicates from current envisioning of line 45
    T = []
    E = [(u, v) for (u, v) in edges if u in s1 and v in s2 or u in s2 and v in s1]
    
    while s2:
        min_edge = min(E, key = lambda x: lattice.get_edge_data(*x)['weight'])
        T.append(edge)
        E.remove(edge)
        (u, v) = edge
        if u in s2:
            s2.remove(u)
            s1.append(u)
            #This implementation will remove edges that belong to 2 covered nodes. E.g. (1,2) edge in baeldung example. Adjusted since
            E_ = [(u,v) for (u,v) in edges if u in s1 and v in s2 or u in s2 and v in s1]
            E.update(E_)
        else:
            s2.remove(v)
            s1.append(v)
            E = [(u,v) for (u,v) in edges if u in s1 and v in s2 or u in s2 and v in s1]
            E.update(E_)
    return T;

print(_testgraph()[0][1])