# Exercício 19: Dada uma matriz B, de 10 linhas por 20 colunas, escrever um algoritmo que calcula
# e imprima o somatório dos elementos da quinta linha.

B = []

for i in range(10):
    linha = []
    for j in range(20):
        linha.append(int(input(f'Digite B[{i}][{j}]: ')))
    B.append(linha)

soma_linha_5 = sum(B[4])
print(f'O somatório dos elementos da quinta linha: {soma_linha_5}')

