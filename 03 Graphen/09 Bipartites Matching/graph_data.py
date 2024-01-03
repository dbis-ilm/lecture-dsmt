import networkx as nx
import re


small_G = nx.Graph()
small_G.add_edge('A', '1')
small_G.add_edge('B', '1')
small_G.add_edge('B', '2')
small_G.add_edge('C', '2')
small_G.add_edge('B', '2')
small_G.add_edge('C', '2')
small_G.add_edge('C', '3')
small_G.add_edge('C', '4')
small_G.add_edge('D', '4')


flow_G = nx.DiGraph()
flow_G.add_edge('s', 'A', capacity=1)
flow_G.add_edge('s', 'B', capacity=1)
flow_G.add_edge('s', 'C', capacity=1)
flow_G.add_edge('s', 'D', capacity=1)
flow_G.add_edge('A', '1', capacity=1)
flow_G.add_edge('B', '1', capacity=1)
flow_G.add_edge('B', '2', capacity=1)
flow_G.add_edge('C', '2', capacity=1)
flow_G.add_edge('B', '2', capacity=1)
flow_G.add_edge('C', '2', capacity=1)
flow_G.add_edge('C', '3', capacity=1)
flow_G.add_edge('C', '4', capacity=1)
flow_G.add_edge('D', '4', capacity=1)
flow_G.add_edge('1', 't', capacity=1)
flow_G.add_edge('2', 't', capacity=1)
flow_G.add_edge('3', 't', capacity=1)
flow_G.add_edge('4', 't', capacity=1)


def draw(G):
    nodes = [node for node in G if re.fullmatch(r'[A-Za-z]+', node)]

    pos = nx.bipartite_layout(G, nodes)
    nx.draw(G, pos, with_labels=True, font_color='whitesmoke')
