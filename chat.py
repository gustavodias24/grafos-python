import networkx as nx
import matplotlib.pyplot as plt

# Sequência e tamanho dos substrings
sequence = "ATGGAAGTCGCGGAATC"
merns = 7

# Criação do grafo
grafo = nx.DiGraph()

# Adiciona os vértices ao grafo
nodes = []
for i in range(len(sequence) - (merns - 1)):
    nodes.append(sequence[i: i + merns])
    grafo.add_node(nodes[-1])

# Adiciona as arestas consecutivas
for i in range(len(nodes) - 1):
    grafo.add_edge(nodes[i], nodes[i + 1])

# Adiciona a aresta circular
grafo.add_edge(nodes[-1], nodes[0])

# Desenha o grafo
plt.figure(2)
nx.draw_networkx(grafo, pos=nx.spring_layout(grafo), with_labels=True)
plt.show()

# Busca em profundidade para encontrar o maior passeio
passeio_atual = []
passeio_maximo = []
visitados = set()


def dfs(grafo, no):
    global passeio_atual
    global passeio_maximo
    global visitados

    visitados.add(no)
    passeio_atual.append(no)

    for vizinho in grafo.neighbors(no):
        if vizinho not in visitados:
            dfs(grafo, vizinho)

    if len(passeio_atual) > len(passeio_maximo):
        passeio_maximo = passeio_atual.copy()

    passeio_atual.pop()
    visitados.remove(no)


dfs(grafo, nodes[0])
print(passeio_maximo)