import networkx as nx


G = nx.DiGraph()
G.add_edge('s', 'a', capacity=3)
G.add_edge('s', 'b', capacity=1)
G.add_edge('a', 't', capacity=1)
G.add_edge('b', 't', capacity=4)
G.add_edge('a', 'b', capacity=2)

G2 = nx.DiGraph()
G2.add_edge('s', 'a', capacity=100)
G2.add_edge('s', 'b', capacity=100)
G2.add_edge('a', 't', capacity=100)
G2.add_edge('b', 't', capacity=100)
G2.add_edge('a', 'b', capacity=1)
