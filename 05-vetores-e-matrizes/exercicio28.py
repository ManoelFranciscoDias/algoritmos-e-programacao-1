# Exercício 28: Faça um algoritmo que monte uma estrutura de dados homogênea 10 x 30, onde o
# conteúdo de cada elemento é igual à soma dos valores de seus índices.

estrutura = []
for i in range(10):
    linha = []
    for j in range(30):
        linha.append(i + j)
    estrutura.append(linha)

print('Conteúdo da estrutura:')
for linha in estrutura:
    print(' '.join(f'{elemento:4}' for elemento in linha))
