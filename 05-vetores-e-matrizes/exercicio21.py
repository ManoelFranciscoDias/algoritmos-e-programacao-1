# Exercício 21: Elabore um algoritmo que leia uma matriz 4 x 4 e escreva a matriz resultante
# após ter multiplicado os elementos da diagonal principal por uma constante k.

matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f'Digite o elemento [{i}][{j}] da matriz: ')))
    matriz.append(linha)

k = int(input('Informe qual é a constante k: '))

for i in range(4):
    matriz[i][i] *= k

print('Conteúdo da matriz:')
for i in range(4):
    for j in range(4):
        print(f'{matriz[i][j]:4}', end="")
    print()