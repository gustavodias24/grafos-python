SEQUENCE = 'AAAGGCGTTGAGGTT'

# Criar um dicionário para representar o grafo
graph = {}

# Loop sobre as subsequências de tamanho 3
for i in range(len(SEQUENCE)-2):
    # Obter as duas subsequências adjacentes
    seq1 = SEQUENCE[i:i+3]
    seq2 = SEQUENCE[i+1:i+4]

    # Adicionar uma aresta entre as duas subsequências
    if seq1 not in graph:
        graph[seq1] = []
    graph[seq1].append(seq2)

# Verificar se o grafo é euleriano
odd_degree_nodes = [node for node in graph if len(graph[node]) % 2 == 1]
if len(odd_degree_nodes) != 2:
    print("O grafo não é euleriano")
else:
    # Encontrar um circuito euleriano
    start_node = odd_degree_nodes[0]
    circuit = [start_node]
    while len(circuit) < len(SEQUENCE) // 3 + 1:
        node = circuit[-1]
        next_node = graph[node][0]
        circuit.append(next_node)
        graph[node].remove(next_node)
        graph[next_node].remove(node)
    # Juntar as subsequências do circuito
    reconstructed_sequence = circuit[0] + "".join([node[-1] for node in circuit[1:]])
    print(reconstructed_sequence)