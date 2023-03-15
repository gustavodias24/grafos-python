sequencia = "AAAGGCGTTGAGGTT"
salto = 4
vertices = []

for i in range(len(sequencia) - (salto - 1)):
    vertices.append(sequencia[i:i + salto])

# construir matriz adjacente
n = len(vertices)
adj = [[0] * n for i in range(n)]


for i in range(n):
    for j in range(i + 1, n):
        diff = 0
        for k in range(salto):
            if vertices[i][k] != vertices[j][k]:
                diff += 1
                if diff > 1:
                    break
        if diff == 1:
            adj[i][j] = adj[j][i] = 1


# imprimir matriz adjacente
for i in range(n):
    for j in range(n):
        print(adj[i][j], end=' ')
    print()
