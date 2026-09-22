# Exercício 20: Dada uma tabela de 4 x 5 elementos, calcular a soma de cada linha e a soma de
# todos os elementos.

tabela = []
for i in range(4):
    linha = []
    for j in range(5):
        linha.append(int(input(f'Digite o elemento [{i}][{j}] da tabela: ')))
    tabela.append(linha)

soma_total = 0
for i in range(4):
    soma_linha = sum(tabela[i])
    soma_total += soma_linha
    print(f'A soma da {i+1}ª linha é: {soma_linha}')

print(f'A soma de todos os elementos é: {soma_total}')