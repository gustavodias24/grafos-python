import networkx as nx
import os

with open('arquivo.fastq', 'r') as file:
    # Lendo as linhas do arquivo e armazenando em uma lista
    linhas = file.readlines()

    # Dividindo a lista em sub-listas de 4 em 4 linhas
    sub_listas = [linhas[i:i + 4] for i in range(0, len(linhas), 4)]

    # list de sequencia
    lista_sequencia = []

    # salva o segundo item de cada sub-lista
    for sub_lista in sub_listas:
        # print(sub_lista[1].strip())
        lista_sequencia.append(sub_lista[1].strip())

    # criando o grafo
    grafo = nx.DiGraph()

    # Adicionando nós com arestas adjacentes
    mers = 4

    all_nos = []
    for seq in lista_sequencia:
        lista_nos = []

        for i in range(len(seq) - (mers - 1)):

            if seq[i: i + mers] not in all_nos:
                all_nos.append(seq[i: i + mers])

            grafo.add_node(seq[i: i + mers])
            lista_nos.append(seq[i: i + mers])

        for i in range(len(lista_nos) - 1):
            grafo.add_edge(lista_nos[i], lista_nos[i + 1])

    print("euleriano:", nx.is_eulerian(grafo))

    maior_caminho_len = 0
    maior_caminho = []
    for no_origem in range(len(all_nos)):
        for no_destino in range(len(all_nos)):
            print("({}, {})".format(all_nos[no_origem], all_nos[no_destino]))
            # if nx.has_path(grafo, all_nos[no_origem], all_nos[no_destino]):
            for c in nx.all_simple_paths(grafo, all_nos[no_origem], all_nos[no_destino]):
                if len(c) > maior_caminho_len:
                    os.system("cls")
                    maior_caminho_len = len(c)
                    maior_caminho = c
                    print("maior_caminho_len:", maior_caminho_len)
                    print("maior_caminho:", maior_caminho)

                break
            break

    os.system("cls")
    print("maior_caminho_len:", maior_caminho_len)
    print("maior_caminho:", maior_caminho)
