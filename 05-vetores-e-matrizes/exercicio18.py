# Exercício 18: Faça um algoritmo qualquer que leia uma matriz A de 15 linhas por 25 colunas e
# imprima o seu conteúdo.

A = []
for i in range(15):
    linha = []
    for j in range(25):
        valor = int(input(f'Digite A[{i}][{j}]: '))
        linha.append(valor)
    A.append(linha)


print('Conteudo da matriz A: ')
for i in range(15):
    for j in range(25):
        print(f"{A[i][j]:4}", end="")
    print()        