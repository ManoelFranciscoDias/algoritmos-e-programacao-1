# Exercício 24: Escreva um algoritmo que leia duas matrizes reais de dimensão 3 x 5, calcule e
# imprima a sua soma.

matrizA = []
matrizB = []

print('MATRIZ A')
for i in range(3):
    linha = []
    for j in range(5):
        linha.append(float(input(f'Digite o elemento A[{i}][{j}]: ')))
    matrizA.append(linha)

print('MATRIZ B')
for i in range(3):
    linha = []
    for j in range(5):
        linha.append(float(input(f'Digite o elemento B[{i}][{j}]: ')))
    matrizB.append(linha)

matrizC = []

for i in range(3):
    linha = []
    for j in range(5):
        linha.append(matrizA[i][j] + matrizB[i][j])
    matrizC.append(linha)

print('MATRIZ C (soma de A com B)')
for i in range(3):
    for j in range(5):
        print(f'{matrizC[i][j]:6.2f}', end='')
    print()