import networkx as nx
import matplotlib.pyplot as plt
from typing import Set


cities = nx.Graph()
cities.add_edge('Eisenach', 'Ruhla', weight=20)
cities.add_edge('Eisenach', 'Waltershausen', weight=25)
cities.add_edge('Eisenach', 'Gehlberg', weight=25)
cities.add_edge('Eisenach', 'Friedrichroda', weight=30)
cities.add_edge('Ruhla', 'TambachDietharz', weight=25)
cities.add_edge('Ruhla', 'Waltershausen', weight=20)
cities.add_edge('Gehlberg', 'TambachDietharz', weight=15)
cities.add_edge('Gehlberg', 'Friedrichroda', weight=25)
cities.add_edge('Friedrichroda', 'Gehren', weight=25)
cities.add_edge('Ilmenau', 'Oberhof', weight=25)
cities.add_edge('Ilmenau', 'TambachDietharz', weight=30)
cities.add_edge('Ilmenau', 'ZellaMehlis', weight=25)
cities.add_edge('Oberhof', 'Suhl', weight=15)
cities.add_edge('Oberhof', 'Lauscha', weight=35)
cities.add_edge('TambachDietharz', 'Gotha', weight=55)
cities.add_edge('Suhl', 'ZellaMehlis', weight=10)
cities.add_edge('Suhl', 'Meiningen', weight=40)
cities.add_edge('Meiningen', 'Schleusingen', weight=30)
cities.add_edge('Schleusingen', 'Gotha', weight=50)
cities.add_edge('Schleusingen', 'NeuhausAR', weight=20)
cities.add_edge('Schleusingen', 'Hildburghausen', weight=15)
cities.add_edge('Masserberg', 'NeuhausAR', weight=20)
cities.add_edge('NeuhausAR', 'Lauscha', weight=35)
cities.add_edge('NeuhausAR', 'Oberhof', weight=55)
cities.add_edge('Lauscha', 'Sonneberg', weight=15)
cities.add_edge('Lauscha', 'Steinach', weight=15)
cities.add_edge('Sonneberg', 'Steinach', weight=15)
cities.add_edge('Gotha', 'Hildburghausen', weight=75)
cities.add_edge('Ilmenau', 'Lauscha', weight=40)
cities.add_edge('Ilmenau', 'Ruhla', weight=60)
cities.add_edge('TambachDietharz', 'Suhl', weight=40)
cities.add_edge('TambachDietharz', 'Meiningen', weight=45)

def draw_cities(graph: nx.Graph):
    pos = {
        'Eisenach': [1159.7633, -93.43375],
        'Ruhla': [986.3215, -16.088493],
        'Waltershausen': [1164.3373, 56.28163],
        'Gehlberg': [1021.95105, -175.97806],
        'Friedrichroda': [1267.1681, -230.15562],
        'Ilmenau': [450.01358, 38.451418],
        'Oberhof': [100.38327, 59.167953],
        'TambachDietharz': [724.0116, -88.65561],
        'Suhl': [7.873535, -75.329346],
        'ZellaMehlis': [204.26312, -11.835753],
        'Meiningen': [107.97316, -141.75964],
        'Schleusingen': [-53.44452, -239.20679],
        'Gotha': [404.65103, -196.93806],
        'Gehren': [1468.7135, -305.78067],
        'Masserberg': [-302.45526, -53.65928],
        'NeuhausAR': [-170.47804, 25.456665],
        'Lauscha': [-88.82424, 221.96655],
        'Sonneberg': [149.33255, 280.05417],
        'Steinach': [-239.35443, 320.05417],
        'Hildburghausen': [115.84885, -334.47046]
    }

    nx.draw(graph, pos=pos, node_size=100, node_color='#EEE2DE')
    nx.draw_networkx_labels(graph, pos, font_size=7)

    edge_labels = {(u, v): d['weight'] for u, v, d in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels, font_size=6)

    plt.show()
    plt.close()


exams = nx.DiGraph()
exams.add_edge('G1', 'Mo 09:30', weight=0)
exams.add_edge('G1', 'Mo 10:00', weight=0)
exams.add_edge('G1', 'Mo 10:30', weight=0)
exams.add_edge('G1', 'Di 12:00', weight=0)
exams.add_edge('G2', 'Do 11:30', weight=1)
exams.add_edge('G2', 'Do 12:30', weight=1)
exams.add_edge('G2', 'Di 11:30', weight=0)
exams.add_edge('G2', 'Mi 11:00', weight=0)
exams.add_edge('G2', 'Do 12:00', weight=1)
exams.add_edge('G2', 'Di 12:30', weight=0)
exams.add_edge('G2', 'Mi 10:30', weight=0)
exams.add_edge('G2', 'Di 12:00', weight=0)
exams.add_edge('G3', 'Di 09:30', weight=0)
exams.add_edge('G3', 'Di 10:00', weight=0)
exams.add_edge('G3', 'Do 11:30', weight=0)
exams.add_edge('G3', 'Di 09:00', weight=0)
exams.add_edge('G3', 'Do 12:00', weight=0)
exams.add_edge('G3', 'Do 11:00', weight=0)
exams.add_edge('G3', 'Mi 09:00', weight=1)
exams.add_edge('G3', 'Mi 09:30', weight=1)
exams.add_edge('G4', 'Do 12:30', weight=0)
exams.add_edge('G4', 'Do 11:30', weight=0)
exams.add_edge('G4', 'Do 12:00', weight=0)
exams.add_edge('G4', 'Do 11:00', weight=0)
exams.add_edge('G5', 'Mi 10:00', weight=0)
exams.add_edge('G5', 'Mi 09:00', weight=0)
exams.add_edge('G5', 'Mi 10:30', weight=0)
exams.add_edge('G5', 'Mi 09:30', weight=0)
exams.add_edge('G6', 'Di 09:30', weight=0)
exams.add_edge('G6', 'Di 11:00', weight=0)
exams.add_edge('G6', 'Di 09:00', weight=0)
exams.add_edge('G6', 'Di 11:30', weight=0)
exams.add_edge('G6', 'Di 10:30', weight=0)
exams.add_edge('G6', 'Di 10:00', weight=0)
exams.add_edge('G7', 'Do 12:30', weight=0)
exams.add_edge('G7', 'Mi 11:00', weight=0)
exams.add_edge('G8', 'Mo 09:00', weight=0)
exams.add_edge('G8', 'Mo 09:30', weight=0)
exams.add_edge('G8', 'Mo 10:00', weight=0)
exams.add_edge('G8', 'Di 09:00', weight=0)
exams.add_edge('G8', 'Mi 09:00', weight=1)
exams.add_edge('G8', 'Mo 10:30', weight=0)
exams.add_edge('G8', 'Di 09:30', weight=0)
exams.add_edge('G8', 'Mi 10:00', weight=1)
exams.add_edge('G8', 'Mi 11:00', weight=1)
exams.add_edge('G8', 'Di 10:00', weight=0)
exams.add_edge('G8', 'Mi 10:30', weight=1)
exams.add_edge('G8', 'Mi 09:30', weight=1)
exams.add_edge('G9', 'Mi 10:00', weight=0)
exams.add_edge('G9', 'Mo 09:00', weight=0)
exams.add_edge('G9', 'Mo 09:30', weight=0)
exams.add_edge('G9', 'Mo 10:00', weight=0)
exams.add_edge('G9', 'Mi 09:00', weight=0)
exams.add_edge('G9', 'Mi 09:30', weight=0)
exams.add_edge('G9', 'Mo 10:30', weight=0)
exams.add_edge('G10', 'Mi 10:00', weight=0)
exams.add_edge('G10', 'Mi 09:00', weight=0)
exams.add_edge('G10', 'Mi 09:30', weight=0)
exams.add_edge('G10', 'Di 12:30', weight=1)
exams.add_edge('G11', 'Di 09:30', weight=0)
exams.add_edge('G11', 'Di 10:00', weight=0)
exams.add_edge('G11', 'Mo 09:00', weight=0)
exams.add_edge('G11', 'Mo 09:30', weight=0)
exams.add_edge('G11', 'Mo 10:00', weight=0)
exams.add_edge('G11', 'Di 09:00', weight=0)
exams.add_edge('G12', 'Di 11:00', weight=0)
exams.add_edge('G12', 'Di 09:00', weight=0)
exams.add_edge('G12', 'Di 11:30', weight=0)
exams.add_edge('G12', 'Di 12:00', weight=0)
exams.add_edge('G12', 'Di 09:30', weight=0)
exams.add_edge('G12', 'Di 12:30', weight=0)
exams.add_edge('G12', 'Di 10:30', weight=0)
exams.add_edge('G12', 'Di 10:00', weight=0)
exams.add_edge('G13', 'Di 11:00', weight=0)
exams.add_edge('G13', 'Di 12:30', weight=0)
exams.add_edge('G13', 'Di 11:30', weight=0)
exams.add_edge('G13', 'Di 12:00', weight=0)
exams.add_edge('G14', 'Di 09:30', weight=0)
exams.add_edge('G14', 'Mo 09:00', weight=1)
exams.add_edge('G14', 'Mo 09:30', weight=1)
exams.add_edge('G14', 'Mo 10:00', weight=1)
exams.add_edge('G14', 'Do 11:30', weight=0)
exams.add_edge('G14', 'Di 09:00', weight=0)
exams.add_edge('G14', 'Do 11:00', weight=0)
exams.add_edge('G14', 'Di 10:30', weight=0)
exams.add_edge('G14', 'Di 10:00', weight=0)
exams.add_edge('G14', 'Mo 10:30', weight=1)
exams.add_edge('G14', 'Di 11:00', weight=1)
exams.add_edge('G14', 'Do 12:30', weight=1)
exams.add_edge('G14', 'Di 11:30', weight=1)
exams.add_edge('G14', 'Do 12:00', weight=1)
exams.add_edge('G14', 'Mi 10:30', weight=1)
exams.add_edge('G15', 'Mi 10:00', weight=0)
exams.add_edge('G15', 'Mi 09:00', weight=0)
exams.add_edge('G15', 'Mi 09:30', weight=0)
exams.add_edge('G16', 'Di 09:30', weight=0)
exams.add_edge('G16', 'Mi 10:00', weight=0)
exams.add_edge('G16', 'Mo 09:00', weight=1)
exams.add_edge('G16', 'Mo 09:30', weight=1)
exams.add_edge('G16', 'Mo 10:00', weight=1)
exams.add_edge('G16', 'Di 09:00', weight=0)
exams.add_edge('G16', 'Mi 09:00', weight=0)
exams.add_edge('G16', 'Di 10:00', weight=0)
exams.add_edge('G16', 'Mi 09:30', weight=0)
exams.add_edge('G16', 'Mo 10:30', weight=1)
exams.add_edge('G17', 'Do 11:30', weight=0)

def draw_exams(graph: nx.DiGraph, source: str = 's', target: str = 't'):
    st = source, target
    left = set(_filter_exams_nodes(graph))

    # initialize figure
    plt.figure(figsize=(8, 11))

    # layout without source and target
    copy = graph.copy()
    copy.remove_nodes_from(st)
    pos = nx.bipartite_layout(copy, left)

    # add positions for source and target
    xs = [x for x, _ in pos.values()]
    ys = [y for _, y in pos.values()]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    dx, dy = max_x - min_x, max_y - min_y

    pos[source] = [min_x - dx / 3, max_y - dy / 2]
    pos[target] = [max_x + dx / 3, max_y - dy / 2]

    # sort other nodes
    for a in sorted(pos.keys(), key=_sort_exams_nodes):
        for b in sorted(pos.keys(), key=_sort_exams_nodes):
            if a in left and b not in left or a not in left and b in left or a in st or b in st:
                continue

            if pos[a][1] > pos[b][1]:
                pos[a], pos[b] = pos[b], pos[a]

    # draw graph
    nx.draw(graph, pos, with_labels=True, font_size=6, font_color='whitesmoke', node_size=1000)
    nx.draw_networkx_edge_labels(graph, pos, nx.get_edge_attributes(graph, 'weight'), font_size=6)

    # display image
    plt.show()
    plt.close()

def _filter_exams_nodes(graph: nx.DiGraph):
    for node in graph.nodes:
       if node.startswith('G'):
           yield node

def _sort_exams_nodes(node):
    if node.startswith('G'):
        return f'G{int(node[1:]):03}'
    if node.startswith('Mo '):
        return f'W1 {node[3:]}'
    if node.startswith('Di '):
        return f'W2 {node[3:]}'
    if node.startswith('Mi '):
        return f'W3 {node[3:]}'
    if node.startswith('Do '):
        return f'W4 {node[3:]}'
    else:
        return node
