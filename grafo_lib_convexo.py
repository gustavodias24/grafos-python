import networkx as nx
import matplotlib.pyplot as plt

sequence = "ATAGGATA"
merns = 4
grafo = nx.DiGraph()


# funcao generica pra add no
def add_nos(s):
    # adiciona nós
    nos = []
    for i in range(len(s) - (merns - 1)):
        read = s[i: i + merns]
        nos.append(read)
        # print(" " * i, read)
        grafo.add_node(read)

    # adiciona arestas adjacentes com o próximo nó
    for i in range(len(nos) - 1):
        grafo.add_edge(nos[i], nos[i + 1])

    return nos


# funcao generica pra add novos no
def add_novos_nos(nos_anteriores):
    new_sequence = ""
    for n in nos_anteriores:
        new_sequence += n

    print(new_sequence)
    # adiciona novos nós ao grafo
    nos = []
    for i in range(len(new_sequence) - (merns - 1)):
        read = new_sequence[i: i + merns]
        nos.append(read)
        # print(" " * i, read)
        grafo.add_node(read)

    # adiciona aresta adjacentes com o próximo nó ( novos nós)
    for i in range(len(nos) - 1):
        grafo.add_edge(nos[i], nos[i + 1])

    return nos


# repete a quantidade de reads geradas
while True:

    nos = add_nos(sequence)
    for i in range(len(nos)):
        nos = add_novos_nos(nos)

    break

# Desenha o grafo
plt.figure(2)
nx.draw_networkx(grafo, pos=nx.spring_layout(grafo), with_labels=True)
plt.show()



