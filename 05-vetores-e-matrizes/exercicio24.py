# Exercício 24: Escreva um algoritmo que leia duas matrizes reais de dimensão 3 x 5, calcule e
# imprima a sua soma.

matriz_a = []
matriz_b = []

print('MATRIZ A')
for i in range(3):
    linha = []
    for j in range(5):
        linha.append(float(input(f'Digite o elemento A[{i}][{j}]: ')))
    matriz_a.append(linha)

print('MATRIZ B')
for i in range(3):
    linha = []
    for j in range(5):
        linha.append(float(input(f'Digite o elemento B[{i}][{j}]: ')))
    matriz_b.append(linha)

matriz_c = []

for i in range(3):
    linha = []
    for j in range(5):
        linha.append(matriz_a[i][j] + matriz_b[i][j])
    matriz_c.append(linha)

print('MATRIZ C (soma de A com B)')
for i in range(3):
    for j in range(5):
        print(f'{matriz_c[i][j]:6.2f}', end='')
    print()
