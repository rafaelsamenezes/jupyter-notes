import networkx as nx
import matplotlib.pyplot as plt

# BOILERPLATE
def draw_graph(graph):
    pos=nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(graph,'weight')
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)

def create_graph(V,E):
    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_weighted_edges_from(E)
    return G

def has_path(G, V0, V1):
    return nx.has_path(G, V0, V1)

def shortest_path_length(G, V0, V1):
    W = nx.get_edge_attributes(G,'weight')
    return nx.dijkstra_path_length(G, V0, V1)

# Graphs Ready

def city_graph():
    V = ["Manaus", "Boa Vista", "Presidente Figueiredo"]
    E = [("Manaus", "Presidente Figueiredo", 200), ("Presidente Figueiredo", "Boa Vista", 540)]
    return create_graph(V,E)


def print_helper(L):
    return ', '.join(str(e) for e in L)

class CFG:
    def __init__(self, verbose=False):
        self.G = nx.DiGraph()
        self.verbose = verbose

    def add_node(self, N, kill, gen):
        self.G.add_node(N, kill=kill, gen=gen)

    def add_edges(self, edges):
        self.G.add_edges_from(edges)

    def add_edge(self, V0, V1):
        self.G.add_edge(V0, V1)
    # V -> 2^V
    def pred(self, V):
        r = self.G.predecessors(V)
        if(self.verbose):
            print(f"Predecessors of {V} are: {print_helper(r)}")
        return r

    def succ(self, V):
        r = self.G.successors(V)
        if(self.verbose):
            print(f"Successors of {V} are: {print_helper(r)}")
        return r


    def kill(self, V):
        r =  self.G.nodes[V]["kill"]
        if(self.verbose):
            print(f"Vertex '{V}'' kills: {print_helper(r)}")
        return r


    def gen(self, V):
        r =  self.G.nodes[V]["gen"]
        if(self.verbose):
            print(f"Vertex '{V}'' gen: {print_helper(r)}")
        return r
