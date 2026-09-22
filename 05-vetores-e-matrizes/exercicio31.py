# Exercício 31: Preencher e imprimir os elementos de uma matriz A(10 x 6) de elementos reais com
# valores tais que:
# - Se I < J, A[I][J] = I / J;
# - Se I = J, A[I][J] = 0;
# - Se I > J, A[I][J] = J / I;

A = []
for i in range(10):
    linha = []
    for j in range(6):
        if i < j:
            linha.append(i / j)
        elif i == j:
            linha.append(0)
        else:
            linha.append(j / i)
    A.append(linha)

print('Matriz A:')
for linha in A:
    print(' '.join(f'{elemento:6.2f}' for elemento in linha))
