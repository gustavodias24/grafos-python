import networkx as nx

# Criar um grafo direcionado de exemplo
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5)])

# Verificar se o nó 1 tem mais de uma aresta de saída
if G.out_degree(1) > 1:
    print("O nó 1 tem mais de uma aresta de saída.")
else:
    print("O nó 1 tem no máximo uma aresta de saída.")
