# Exercício 27: A tabela dada a seguir contém vários itens que estão estocados em vários
# armazéns de uma companhia. É fornecido, também, o custo de cada um dos produtos armazenados.
#
#                 PRODUTO 1 (unidades)  PRODUTO 2 (unidades)  PRODUTO 3 (unidades)
# ARMAZÉM 1       1200                  3700                  3737
# ARMAZÉM 2       1400                  4210                  4224
# ARMAZÉM 3       2000                  2240                  2444
# CUSTO (R$)      260,00                420,00                330,00
#
# Fazer um algoritmo que:
# a) leia o estoque inicial;
# b) determine e imprima quantos itens estão armazenados em cada armazém;
# c) qual o armazém que possui a maior quantidade de produto 2 armazenado;
# d) o custo total de:
#    d.1) cada produto em cada armazém;
#    d.2) estoque em cada armazém;
#    d.3) cada produto em todos os armazéns.

ARMAZENS = 3
PRODUTOS = 3

estoque = []
print('Digite o estoque inicial')
for i in range(ARMAZENS):
    linha = []
    for j in range(PRODUTOS):
        linha.append(int(input(f'Quantidade do produto {j+1} no armazém {i+1}: ')))
    estoque.append(linha)

custo = []
print('Digite o custo de cada produto')
for j in range(PRODUTOS):
    custo.append(float(input(f'Custo do produto {j+1}: ')))

print('\nItens armazenados em cada armazém:')
for i in range(ARMAZENS):
    total_armazem = 0
    for j in range(PRODUTOS):
        total_armazem += estoque[i][j]
    print(f'Armazém {i+1}: {total_armazem} itens')

armazem_maior_produto2 = 0
for i in range(1, ARMAZENS):
    if estoque[i][1] > estoque[armazem_maior_produto2][1]:
        armazem_maior_produto2 = i
print(f'\nArmazém com maior quantidade do produto 2: Armazém {armazem_maior_produto2 + 1}')

print('\nCusto de cada produto em cada armazém:')
for i in range(ARMAZENS):
    for j in range(PRODUTOS):
        print(f'Armazém {i+1}, Produto {j+1}: R$ {estoque[i][j] * custo[j]:.2f}')

print('\nCusto do estoque em cada armazém:')
for i in range(ARMAZENS):
    custo_armazem = 0
    for j in range(PRODUTOS):
        custo_armazem += estoque[i][j] * custo[j]
    print(f'Armazém {i+1}: R$ {custo_armazem:.2f}')

print('\nCusto de cada produto em todos os armazéns:')
for j in range(PRODUTOS):
    custo_produto = 0
    for i in range(ARMAZENS):
        custo_produto += estoque[i][j] * custo[j]
    print(f'Produto {j+1}: R$ {custo_produto:.2f}')
