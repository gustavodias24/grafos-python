class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiconar_aresta_com_peso(self, u, v, peso):
        self.grafo[u - 1][v - 1] = peso

    def exibir_grafo(self):
        for elem in self.grafo:
            print(elem)


if __name__ == "__main__":
    grafo = Grafo(int(input("Entre com a qtd de vértices do grafo: ")))

    for e in range(int(input("quantidade de aresta: "))):
        grafo.adiconar_aresta_com_peso(
            int(input("u: ")),
            int(input("v: ")),
            int(input("peso: "))
        )

    grafo.exibir_grafo()
