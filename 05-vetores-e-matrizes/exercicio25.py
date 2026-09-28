# Exercício 25: Dada uma matriz MAT de 4 x 5 elementos, faça um algoritmo para somar os elementos
# de cada linha gerando o vetor SOMALINHA. Em seguida, somar os elementos do vetor SOMALINHA na
# variável TOTAL que deve ser impressa no final.

matriz = []

for i in range(4):
    linha = []
    for j in range(5):
        linha.append(int(input(f'Informe o elemento [{i}][{j}] da matriz: ')))
    matriz.append(linha)

soma_linha = []
for i in range(4):
    soma = 0
    for j in range(5):
        soma += matriz[i][j]
    soma_linha.append(soma)

total = 0
for i in range(4):
    total += soma_linha[i]

print(f'Vetor SOMALINHA: {soma_linha}')
print(f'TOTAL: {total}')
