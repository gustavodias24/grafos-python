import networkx as nx
import matplotlib.pyplot as plt

sequence = "ATAGGATA"
merns = 4
grafo = nx.DiGraph()

# adicionar nó central
central_node = "CENTER"
grafo.add_node(central_node)

# função genérica para adicionar nó
def add_node(s, visited_nodes):
    nos = []
    for i in range(len(s) - (merns - 1)):
        read = s[i: i + merns]
        if read not in visited_nodes:
            visited_nodes.add(read)
            nos.append(read)
            grafo.add_node(read)

    # adicionar arestas adjacentes com o próximo nó
    for i in range(len(nos) - 1):
        grafo.add_edge(nos[i], nos[i + 1])

    return nos

# função genérica para adicionar novos nós
def add_new_nodes(previous_nodes, visited_nodes):
    new_sequence = "".join(previous_nodes)
    nos = []
    for i in range(len(new_sequence) - (merns - 1)):
        read = new_sequence[i: i + merns]
        if read not in visited_nodes:
            visited_nodes.add(read)
            nos.append(read)
            grafo.add_node(read)

    # adicionar arestas adjacentes com o próximo nó (novos nós)
    for i in range(len(nos) - 1):
        grafo.add_edge(nos[i], nos[i + 1])

    # adicionar arestas extras para tornar o grafo euleriano
    for node in previous_nodes:
        if grafo.out_degree(node) % 2 == 1:
            grafo.add_edge(node, central_node)

    return nos

# repetir a quantidade de reads geradas
visited_nodes = set([central_node])
previous_nodes = add_node(sequence, visited_nodes)
while previous_nodes:
    new_nodes = add_new_nodes(previous_nodes, visited_nodes)
    if not new_nodes:
        # adicionar arestas extras para tornar o grafo euleriano
        odd_nodes = [node for node in grafo.nodes() if grafo.out_degree(node) % 2 == 1]
        if len(odd_nodes) == 2:
            grafo.add_edge(odd_nodes[0], odd_nodes[1])
        break
    previous_nodes = new_nodes

print(nx.has_eulerian_path(grafo))
# desenhar o grafo
plt.figure(figsize=(12, 8))
pos = nx.kamada_kawai_layout(grafo)
nx.draw_networkx_nodes(grafo, pos, nodelist=[central_node], node_color='r', node_size=1000)
nx.draw_networkx_labels(grafo, pos, font_size=12, font_family='sans-serif')
nx.draw_networkx_edges(grafo, pos, edge_color='k', width=1)
plt.axis('off')
plt.show()
