class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adicionar_aresta(self, u, v):
        # grafo direcionado
        self.grafo[u - 1][v - 1] = 1  # contar as aresta seria += 1
        # self.grafo[v - 1][u - 1] = 1 Grafo simples ( simétrico )

    def exibir_grafo(self):
        for elem in self.grafo:
            print(elem)


if __name__ == "__main__":
    grafo = Grafo(4)
    grafo.adicionar_aresta(1, 2)
    grafo.adicionar_aresta(4, 3)
    grafo.exibir_grafo()
