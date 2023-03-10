class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adicionar_aresta(self, u, v):
        # Grafo não direcionado que pode ser multigrafo e contar as arestas
        self.grafo[u - 1][v - 1] += 1
        if u != v:  # por causa de laços
            self.grafo[v - 1][u - 1] += 1

    def tem_aresta(self, u, v):
        if self.grafo[u - 1][v - 1] == 0:
            print("Sem aresta")
        else:
            print(f'Tem {self.grafo[u - 1][v - 1]} aresta na linha {u} coluna {v}')

    def eh_euleriano(self):
        contador = 0
        for i in range(self.vertices):
            grau = 0
            for j in range(self.vertices):
                if i == j:
                    grau = grau + 2 * self.grafo[i][j]
                else:
                    grau += self.grafo[i][j]

            if grau % 2 != 0:
                contador += 1

        if contador == 0:
            print('É um grafo euleriano!')
        elif contador == 2:

            print('É um grafo semieuleriano!')
        elif contador > 2:
            print('O grafo não é euleriano e nem semieulariano!')

    def exibir_grafo(self):
        for elem in self.grafo:
            print(elem)


if __name__ == "__main__":
    g = Grafo(4)

    # semi euleriano #
    # g.adicionar_aresta(1, 2)
    # g.adicionar_aresta(3, 4)
    # g.adicionar_aresta(2, 3)  # laço

    # euleriano #
    # g.adicionar_aresta(4, 1)
    # g.adicionar_aresta(1, 2)
    # g.adicionar_aresta(3, 4)
    # g.adicionar_aresta(2, 3)  # laço

    # nem um nem outro #
    g.adicionar_aresta(1, 3)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(2, 3)
    g.adicionar_aresta(2, 3)
    g.adicionar_aresta(2, 3)
    g.adicionar_aresta(3, 4)
    g.adicionar_aresta(3, 4)
    g.adicionar_aresta(3, 4)
    g.adicionar_aresta(3, 4)
    g.adicionar_aresta(3, 4)
    g.adicionar_aresta(4, 1)
    g.adicionar_aresta(4, 1)
    g.adicionar_aresta(4, 1)
    g.adicionar_aresta(4, 1)

    g.exibir_grafo()
    g.eh_euleriano()
