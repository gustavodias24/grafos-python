import networkx as nx
import os
grafo = nx.DiGraph()
grafo.add_edges_from([(1,2), (2,3), (3,4), (2,5), (5,4)])


for caminho in [g for g in nx.all_simple_paths(grafo, 1, 5)]:
    os.system("cls")
    print(len(caminho))