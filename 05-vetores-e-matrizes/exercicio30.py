# Exercício 30: Suponha que nos é dada uma matriz de inteiros A com m=20 linhas e n=30 colunas, e
# um vetor de inteiros X com n=30 elementos. Deseja-se gerar um novo vetor de inteiros Y, formado
# a partir das seguintes operações:
# Y[0]   = A[0][0]   * X[0] + A[0][1]   * X[1] + ... + A[0][n-1]   * X[n-1]
# Y[1]   = A[1][0]   * X[0] + A[1][1]   * X[1] + ... + A[1][n-1]   * X[n-1]
# ...
# Y[m-1] = A[m-1][0] * X[0] + A[m-1][1] * X[1] + ... + A[m-1][n-1] * X[n-1]
# Escreva os dados de entrada (os valores de A e X) seguidos pelos valores dos elementos de Y.

M = 20
N = 30

A = []
print('Digite os elementos da matriz A')
for i in range(M):
    linha = []
    for j in range(N):
        linha.append(int(input(f'Digite A[{i}][{j}]: ')))
    A.append(linha)

X = []
print('Digite os elementos do vetor X')
for j in range(N):
    X.append(int(input(f'Digite X[{j}]: ')))

Y = []
for i in range(M):
    soma = 0
    for j in range(N):
        soma += A[i][j] * X[j]
    Y.append(soma)

print('Matriz A:', A)
print('Vetor X:', X)
print('Vetor Y:', Y)
