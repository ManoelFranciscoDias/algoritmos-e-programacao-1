# Exercício 22: Escreva um algoritmo que:
# a) leia uma matriz quadrada 20 x 20 de elementos reais;
# b) divida cada elemento de uma linha da matriz pelo elemento da diagonal principal dessa linha;
# c) imprima a matriz assim modificada.

matriz = []
for i in range(20):
    linha = []
    for j in range(20):
        linha.append(float(input(f'Informe o elemento [{i}][{j}] da matriz: ')))
    matriz.append(linha)

for i in range(20):
    diagonal = matriz[i][i]
    if diagonal == 0:
        print(f'Linha {i} não pode ser dividida: elemento da diagonal é zero.')
        continue
    for j in range(20):
        matriz[i][j] /= diagonal

print('Matriz modificada:')
for linha in matriz:
    print(' '.join(f'{elemento:8.2f}' for elemento in linha))