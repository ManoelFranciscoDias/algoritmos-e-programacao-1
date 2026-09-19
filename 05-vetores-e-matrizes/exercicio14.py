# Exercício 14: Um armazém trabalha com 100 mercadorias diferentes identificadas pelos números
# inteiros de 0 a 99. O dono do armazém anota a quantidade de cada mercadoria vendida durante o
# mês. Ele tem uma tabela mensal que indica para cada mercadoria o preço de venda. Escreva o
# algoritmo para calcular o faturamento mensal do armazém, isto é:
# FATURAMENTO = somatório de (QUANTIDADE[i] * PREÇO[i]), para i de 0 a 99.
# As tabelas de preço e quantidade são fornecidas em dois vetores

preco = []
quantidade = []
faturamento = 0

print('Digite o preço de cada mercadoria')
for i in range(100):
    preco.append(float(input(f'Preço da mercadoria {i}: ')))

print('Digite a quantidade vendida de cada mercadoria')
for i in range(100):
    quantidade.append(int(input(f'Quantidade vendida da mercadoria {i}: ')))

for i in range(100):
    faturamento += quantidade[i] * preco[i]

print(f'Faturamento mensal: R$ {faturamento:.2f}')