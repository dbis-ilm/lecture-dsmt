import networkx as nx
import re

from itertools import chain, combinations


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def neighbors(G, N):
    nbs = set()
    for node in N:
        nbs.update(G.neighbors(node))

    return nbs


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
