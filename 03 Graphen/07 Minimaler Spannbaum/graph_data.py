import networkx as nx

G = nx.Graph()
G.add_edge('Eisenach', 'Ruhla', weight=20)
G.add_edge('Eisenach', 'Waltershausen', weight=25)
G.add_edge('Eisenach', 'Gehlberg', weight=25)
G.add_edge('Eisenach', 'Friedrichroda', weight=30)
G.add_edge('Ruhla', 'TambachDietharz', weight=25)
G.add_edge('Ruhla', 'Waltershausen', weight=20)
G.add_edge('Gehlberg', 'TambachDietharz', weight=15)
G.add_edge('Gehlberg', 'Friedrichroda', weight=25)
G.add_edge('Friedrichroda', 'Gehren', weight=25)
G.add_edge('Ilmenau', 'Oberhof', weight=25)
G.add_edge('Ilmenau', 'TambachDietharz', weight=30)
G.add_edge('Ilmenau', 'ZellaMehlis', weight=25)
G.add_edge('Oberhof', 'Suhl', weight=15)
G.add_edge('Oberhof', 'Lauscha', weight=35)
G.add_edge('TambachDietharz', 'Gotha', weight=55)
G.add_edge('Suhl', 'ZellaMehlis', weight=10)
G.add_edge('Suhl', 'Meiningen', weight=40)
G.add_edge('Meiningen', 'Schleusingen', weight=30)
G.add_edge('Schleusingen', 'Gotha', weight=50)
G.add_edge('Schleusingen', 'NeuhausAR', weight=20)
G.add_edge('Schleusingen', 'Hildburghausen', weight=15)
G.add_edge('Masserberg', 'NeuhausAR', weight=20)
G.add_edge('NeuhausAR', 'Lauscha', weight=35)
G.add_edge('NeuhausAR', 'Oberhof', weight=55)
G.add_edge('Lauscha', 'Sonneberg', weight=15)
G.add_edge('Lauscha', 'Steinach', weight=15)
G.add_edge('Sonneberg', 'Steinach', weight=15)
G.add_edge('Gotha', 'Hildburghausen', weight=75)
G.add_edge('Ilmenau', 'Lauscha', weight=40)
G.add_edge('Ilmenau', 'Ruhla', weight=60)
G.add_edge('TambachDietharz', 'Suhl', weight=40)
G.add_edge('TambachDietharz', 'Meiningen', weight=45)

pos = {'Eisenach': [1159.7633, -93.43375],
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
       'Hildburghausen': [115.84885, -334.47046]}

def draw(G: nx.Graph, pos):
    nx.draw(G, pos=pos, node_size=100, node_color='#EEE2DE')
    nx.draw_networkx_labels(G, pos, font_size=7)

    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, font_size=6)
