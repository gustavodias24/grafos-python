import networkx as nx
import matplotlib.pyplot as plt

# Define a sequência original e o tamanho dos mers
sequence = "ATGGAAGTCGCGGAATC"
merns = 4

# Cria o grafo
grafo = nx.DiGraph()

# Cria uma lista para armazenar os nós
nodes = []

# Adiciona os nós da sequência original
for i in range(len(sequence) - (merns - 1)):
    read = sequence[i: i + merns]
    nodes.append(read)
    print(" " * i, read)
    grafo.add_node(read)

# Adiciona as arestas entre os nós adjacentes
for i in range(len(nodes) - 1):
    grafo.add_edge(nodes[i], nodes[i + 1])

# Adiciona novas sequências para criar um grafo convexo
for i in range(len(nodes) - 2):
    read1 = nodes[i]
    read2 = nodes[i + 1]
    read3 = nodes[i + 2]
    new_read = read1 + read2[1:] + read3[2:]
    nodes.append(new_read)
    print(" " * i, new_read)
    grafo.add_node(new_read)
    grafo.add_edge(read1, new_read)
    grafo.add_edge(new_read, read3)

# Desenha o grafo
plt.figure(2)
nx.draw_networkx(grafo, pos=nx.spring_layout(grafo), with_labels=True)
plt.show()