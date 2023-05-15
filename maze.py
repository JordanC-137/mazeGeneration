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

test_graph = _testgraph()

def get_nodes(graph):
    return list(graph)

    #TODO: for git, create README and explore .gitignore files 
def get_edges(graph):
    return list(graph.edges)

def assign_random_edges():
    for source, destination in lattice.edges():
        lattice[source][destination]['weight'] = random.randint(0, 100)

def draw_graph(route):
    nx.draw(lattice)
    plt.savefig(route)

def minSpanningTree():
    #TODO figure out accessing node in terms of label vs surrounding neighbour data
    tg = _testgraph()
    nodes = get_nodes(test_graph)
    arbit_node = 0
    #nodes = get_nodes()
    #arbit_node = random.choice(nodes)
    s1 = [arbit_node]
    s2 = [i for i in nodes if i is not arbit_node]
    print(f"Starter node {arbit_node}")
    print(f"Nodes: {nodes}")
    print(s2)
"""
    edges = get_edges()
    #T can be a set, to prevent duplicates from current envisioning of line 45
    T = []
    E = [(u, v) for (u, v) in edges if u in s1 and v in s2 or u in s2 and v in s1]
    print(E)
    while s2:
        min_edge = min(E, key = lambda x: tg.get_edge_data(*x)['weight'])
        T.append(min_edge)
        E.remove(min_edge)
        (u, v) = min_edge
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
    return T; """

#print(_testgraph()[0][1])
minSpanningTree()