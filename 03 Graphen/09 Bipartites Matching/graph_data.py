import networkx as nx
import re


small_G = nx.Graph()
small_G.add_edge('1', 'A')
small_G.add_edge('1', 'B')
small_G.add_edge('2', 'B')
small_G.add_edge('2', 'C')
small_G.add_edge('2', 'B')
small_G.add_edge('2', 'C')
small_G.add_edge('3', 'C')
small_G.add_edge('4', 'C')
small_G.add_edge('4', 'D')


def draw(G):
    nodes = [node for node in G if re.fullmatch(r'[A-Za-z]+', node)]

    pos = nx.bipartite_layout(G, nodes)
    nx.draw(G, pos, with_labels=True, font_color='whitesmoke')
