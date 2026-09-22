# Exercício 33: Faça um algoritmo que leia uma matriz QUANT de 10 linhas por 10 colunas e imprima
# as seguintes características:
# a) dê o somatório dos quadrados da 1a coluna;
# b) dê o somatório dos cubos da 2a linha;
# c) dê o somatório dos elementos da diagonal principal;
# d) dê o somatório total dos 100 elementos.

QUANT = []
for i in range(10):
    linha = []
    for j in range(10):
        linha.append(int(input(f'Digite QUANT[{i}][{j}]: ')))
    QUANT.append(linha)

soma_quadrados_coluna1 = 0
for i in range(10):
    soma_quadrados_coluna1 += QUANT[i][0] ** 2

soma_cubos_linha2 = 0
for j in range(10):
    soma_cubos_linha2 += QUANT[1][j] ** 3

soma_diagonal = 0
for i in range(10):
    soma_diagonal += QUANT[i][i]

soma_total = 0
for i in range(10):
    for j in range(10):
        soma_total += QUANT[i][j]

print(f'a) Somatório dos quadrados da 1ª coluna: {soma_quadrados_coluna1}')
print(f'b) Somatório dos cubos da 2ª linha: {soma_cubos_linha2}')
print(f'c) Somatório dos elementos da diagonal principal: {soma_diagonal}')
print(f'd) Somatório total dos 100 elementos: {soma_total}')
