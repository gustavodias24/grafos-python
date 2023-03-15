class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adicionar_aresta(self, u, v):
        self.grafo[u-1][v-1] += 1

        if u != v: # caso seja um laco nao repetir a contagem pois vai ter soh uma aresta
            self.grafo[v - 1][u - 1] += 1



sequencia = "AAAGGCGTTGAGGTT"
salto = 4

# obter os vértices
vertices = []
for i in range(len(sequencia) - (salto - 1)):
    vertices.append(sequencia[i:i + salto])
