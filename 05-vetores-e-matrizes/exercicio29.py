# Exercício 29: Ler duas matrizes A e B, cada uma com 7 linhas e 1 coluna. Construir uma matriz C
# de 7 x 2, onde a primeira coluna deverá ser formada pelos elementos da matriz A e a segunda
# coluna deverá ser formada pelos elementos da matriz B.

A = []
print('Digite os elementos da matriz A (7 linhas, 1 coluna)')
for i in range(7):
    A.append(float(input(f'Digite A[{i}][0]: ')))

B = []
print('Digite os elementos da matriz B (7 linhas, 1 coluna)')
for i in range(7):
    B.append(float(input(f'Digite B[{i}][0]: ')))

C = []
for i in range(7):
    C.append([A[i], B[i]])

print('Matriz C:')
for linha in C:
    print(' '.join(f'{elemento:8.2f}' for elemento in linha))
