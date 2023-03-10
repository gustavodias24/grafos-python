class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adicionar_aresta(self, u, v):
        # para grafos direcionados se fosse grafo simples repetia com o outro vertice
        self.grafo[u - 1].append(v)

    def mostrar_lista(self):
        for i in range(self.vertices):
            print(f'{i + 1}: ', end='  ')
            for j in self.grafo[i]:
                print(f'{j} - >', end=' ')

            print('')


if __name__ == "__main__":
    g = Grafo(4)
    g.adicionar_aresta(1,2)
    g.adicionar_aresta(1,3)
    g.adicionar_aresta(2,3)
    g.adicionar_aresta(4,4)

    g.mostrar_lista()
