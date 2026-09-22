# Exercício 26: Escreva um algoritmo para calcular e imprimir a soma de duas matrizes. Seja
# matriz A (m x n) e a matriz B (n x p). Deverão ser impressas as matrizes A, B e a matriz
# produto obtida (C).
# Obs.: C[i][j] = somatório de A[i][k] * B[k][j], para k de 0 a n-1, com i de 0 a m-1 e j de 0 a
# p-1.

m = int(input('Digite o número de linhas da matriz A (m): '))
n = int(input('Digite o número de colunas de A e de linhas de B (n): '))
p = int(input('Digite o número de colunas da matriz B (p): '))

A = []
print('Digite os elementos da matriz A')
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(float(input(f'Digite A[{i}][{j}]: ')))
    A.append(linha)

B = []
print('Digite os elementos da matriz B')
for i in range(n):
    linha = []
    for j in range(p):
        linha.append(float(input(f'Digite B[{i}][{j}]: ')))
    B.append(linha)

C = []
for i in range(m):
    linha = []
    for j in range(p):
        soma = 0
        for k in range(n):
            soma += A[i][k] * B[k][j]
        linha.append(soma)
    C.append(linha)

print('Matriz A:')
for linha in A:
    print(' '.join(f'{elemento:8.2f}' for elemento in linha))

print('Matriz B:')
for linha in B:
    print(' '.join(f'{elemento:8.2f}' for elemento in linha))

print('Matriz produto C:')
for linha in C:
    print(' '.join(f'{elemento:8.2f}' for elemento in linha))
