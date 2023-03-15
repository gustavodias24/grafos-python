class Vertice:
    def __init__(self, adjacencias, valor=None):
        self.adjacencias = adjacencias
        self.valor = valor


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adicionar_aresta(self, u, v):
        self.grafo[u][v] += 1

    def exibir_grafo(self):
        for l in range(len(self.grafo)):
            for c in range(len(self.grafo)):
                print(self.grafo[l][c], end=" ")

            print()


sequence = "ATAGGATA"
merns = 4
# lista do tipo vertice
all_vertices = []

# funcao generica pra add no
def add_nos(s):
    # adiciona nós
    vertices_local = []
    for i in range(len(s) - (merns - 1)):
        read = s[i: i + merns]
        vertices_local.append(read)
        # print(" " * i, read)
        all_vertices.append(Vertice(adjacencias=[], valor=read))

    # adiciona arestas adjacentes com o próximo nó
    for i in range(len(vertices_local)):
        all_vertices[i].adjacencias.append()

    return nos

