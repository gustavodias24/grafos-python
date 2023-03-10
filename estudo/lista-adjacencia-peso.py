class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adicionar_aresta_com_peso(self, u, v, peso):
        # lista direcional
        self.grafo[u - 1].append([v, peso])

    def exibir_grafo(self):
        for i in range(self.vertices):
            print(f'{i + 1}: ', end=' ')
            for j in self.grafo[i]:
                print(f'{j} ->', end=' ')
            print('')


if __name__ == "__main__":
    g = Grafo(6)
    g.adicionar_aresta_com_peso(6, 4, 2)
    g.adicionar_aresta_com_peso(6, 6, 6)
    g.adicionar_aresta_com_peso(2, 4, 3)
    g.adicionar_aresta_com_peso(3, 1, 4)
    g.exibir_grafo()