import networkx as nx
import matplotlib.pyplot as plt
sequence = "ATGGAAGTCGCGGAATC"

merns = 7

grafo = nx.DiGraph()

nodes = []
for i in range(len(sequence) - (merns - 1)):
    print(" " * i + sequence[i: i + merns])
    nodes.append(sequence[i: i + merns])


[grafo.add_node(node) for node in nodes]

for i in range(len(nodes) - 1):
    grafo.add_edge(nodes[i], nodes[i+1])

plt.figure(2)
nx.draw_networkx(grafo, pos=nx.spring_layout(grafo), with_labels=True)
plt.show()
