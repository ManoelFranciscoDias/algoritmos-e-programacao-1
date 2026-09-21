# Exercício 23: Faça um algoritmo que:
# a) leia uma matriz 10 x 10 de elementos inteiros;
# b) imprima essa matriz;
# c) calcule e imprima a soma dos elementos situados abaixo da diagonal principal da matriz,
#    incluindo os elementos da própria diagonal principal.

matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        linha.append(int(input(f'Informe o elemento [{i}][{j}] da matriz: ')))
    matriz.append(linha)

print()
print('Conteudo da matriz')
for i in range(10):
    for j in range(10):
        print(f'{matriz[i][j]:4}', end='')
    print()

soma = 0
for i in range(10):
    for j in range(i + 1):
        soma += matriz[i][j]

print()
print(f'Soma dos elementos abaixo da diagonal principal (incluindo ela): {soma}')