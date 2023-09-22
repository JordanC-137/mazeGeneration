from audioop import cross
from Matrix import Matrix, Connection


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
    
def pop_minimum_connection(ls):
    indexed_ls = [i for i in enumerate(ls)]
    print(indexed_ls)
    index_of_min_connection, min_connection = min(indexed_ls, key = lambda x: x[1].weight)
    ls.pop(index_of_min_connection)
    return (min_connection,ls)

def cross_set_connections(s1, s2, ls):
    l1 = [i for i in ls if i.x in s1 and i.y in s2]
    l2 = [i for i in ls if i.x in s2 and i.y in s1]
    return l1 + l2

def mst(m):
    s1 = [m.nodes[0]]
    s2 = m.nodes[1:]
    T = []
    edges = m.traverse_connections()
    E = cross_set_connections(s1, s2, edges)


a = Connection(0, 5, 10)
b = Connection(1, 4, 6)
c = Connection(3, 3, 2)
pop_minimum_connection([a,b,c])