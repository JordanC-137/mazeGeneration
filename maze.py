import networkx as nx
import matplotlib.pyplot as plt
import random
import pprint

#https://www.baeldung.com/cs/maze-generation
# TODO export lattice object to seperate Maze class with attributes such as start and end point

L = 3
lattice = nx.grid_2d_graph(L,L)

#Node and eges of baeldung graph
def _testgraph():
    test_graph_edges = [(0, 1, 8), (0, 2, 5), (1,3, 11), (1, 2, 9), (2, 3, 15), (2, 4, 10), (3,4, 7)]
    test_graph_edges = map(lambda x: (x[0], x[1], {"weight": x[2]}), test_graph_edges)
    test_graph = nx.Graph()
    test_graph.add_edges_from(test_graph_edges)
    return test_graph

#TODO Use Graph.adj function as seen at bottom of file to add edge_weights to graph in correct corresponding order.
# Currently g.edges returns values in relation to node magnitude rather than order of addition
def _testgraph2():
    tg = nx.grid_2d_graph(3,3)
    tg[(0, 0)][(0,1)]['weight'] = 5
    tg[(0, 1)][(0,2)]['weight'] = 10
    tg[(0, 0)][(1,0)]['weight'] = 1
    tg[(0, 1)][(1,1)]['weight'] = 6
    tg[(0, 2)][(1,2)]['weight'] = 7
    tg[(1, 0)][(1,1)]['weight'] = 11
    tg[(1, 1)][(1,2)]['weight'] = 5
    tg[(1, 0)][(2,0)]['weight'] = 16
    tg[(1, 1)][(2,1)]['weight'] = 4
    tg[(1, 2)][(2,2)]['weight'] = 3
    tg[(2, 0)][(2,1)]['weight'] = 2
    tg[(2, 1)][(2,2)]['weight'] = 12
    return tg


test_graph = _testgraph()

def get_nodes(graph):
    return list(graph)

    #TODO: for git, create README and explore .gitignore files 
def get_edges(graph):
    return list(graph.edges)

def assign_random_edges():
    for source, destination in lattice.edges():
        lattice[source][destination]['weight'] = random.randint(0, 100)

def draw_graph(route, graph):
    labels = {e: graph.edges[e]['weight'] for e in graph.edges}
    pos = nx.spring_layout(graph, k=5)
    nx.draw(graph)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels = labels)
    plt.savefig(route)

def logSpanTreeValues(s1, s2, T, E):
    print(f"S1: {s1}    S2: {s2}    T: {T}    E: {E}")

def removeIrreleventEdges(x, s1):
    if x[1] in s1 and x[0] in s1:
        return False
    return True

def minSpanningTree():
    #TODO figure out accessing node in terms of label vs surrounding neighbour data
    tg = _testgraph()
    nodes = get_nodes(test_graph)
    arbit_node = 0
    #nodes = get_nodes()
    #arbit_node = random.choice(nodes)
    s1 = {arbit_node}
    s2 = [i for i in nodes if i is not arbit_node]
    s2 = set(s2)
    
    edges = get_edges(test_graph)
    #TODO Adjust to use sets rather than lists
    T = []
    E = [(u, v) for (u, v) in edges if u in s1 and v in s2 or u in s2 and v in s1]
    E = set(E)
    while s2:

        min_edge = min(E, key = lambda x: tg.get_edge_data(*x)['weight'])
        print(f"Min edge: {min_edge}")
        print(f"S1: {s1}")
        print(f"S2: {s2}")
        print(f"T: {T}")
        print(f"E: {E}")
        print()
        T.append(min_edge)
        E.remove(min_edge)
        (u, v) = min_edge
        if u in s2:
            s2.remove(u)
            s1.add(u)
            #This implementation will remove edges that belong to 2 covered nodes. E.g. (1,2) edge in baeldung example. Adjusted since
            E_ = [(u,v) for (u,v) in edges if u in s1 and v in s2 or u in s2 and v in s1]
            E.update(E_)
            E = set(filter(lambda x: removeIrreleventEdges(x, s1), E))
        else:
            s2.remove(v)
            s1.add(v)
            E_ = [(u,v) for (u,v) in edges if u in s1 and v in s2 or u in s2 and v in s1]
            E.update(E_)
            E = set(filter(lambda x: removeIrreleventEdges(x, s1), E))

    print()
    print(f"Final S1: {s1}")
    print(f"Final S2: {s2}")
    print(f"Final E: {E}")
    print(f"Final T: {T}")

graph = _testgraph2()

#ls = [[n, dict] for n, dict in graph.adj]
#print(ls)
#print(graph.adj)
