# Exercício 30: Foi feita uma pesquisa do consumo mensal de energia elétrica em uma determinada
# cidade. Para cada consumidor, são fornecidos os seguintes dados: número de identificação do
# consumidor, quantidade de kWh consumidos durante o mês, código do tipo de consumidor
# (R - residencial, C - comercial, I - industrial). Faça um algoritmo que:
# a) leia o preço do kWh por tipo de consumidor;
# b) leia os dados de n consumidores;
# c) escreva o número de identificação e o total a pagar, para cada consumidor;
# d) escreva a quantidade total de KWh consumida para cada um dos três tipos de consumidores;
# e) escreva a quantidade média geral de consumo.

preco_residencial = float(input('Digite o preço do kWh residencial: '))
preco_comercial = float(input('Digite o preço do kWh comercial: '))
preco_industrial = float(input('Digite o preço do kWh industrial: '))

quantidade_consumidores = int(input('Digite o número de consumidores: '))

total_residencial = 0
total_comercial = 0
total_industrial = 0

for i in range(quantidade_consumidores):
    print(f'\nConsumidor {i + 1}:')
    identificacao = input('Digite o número de identificação: ')
    kwh_consumido = float(input('Digite a quantidade de kWh consumida: '))
    tipo_consumidor = input('Digite o tipo de consumidor (R/C/I): ').strip().upper()

    while tipo_consumidor not in ('R', 'C', 'I'):
        print('Tipo inválido! Digite R, C ou I.')
        tipo_consumidor = input('Digite o tipo de consumidor (R/C/I): ').strip().upper()

    if tipo_consumidor == 'R':
        preco_kwh = preco_residencial
        total_residencial += kwh_consumido
    elif tipo_consumidor == 'C':
        preco_kwh = preco_comercial
        total_comercial += kwh_consumido
    else:
        preco_kwh = preco_industrial
        total_industrial += kwh_consumido

    total_pagar = kwh_consumido * preco_kwh
    print(f'Consumidor {identificacao}, total a pagar: R$ {total_pagar:.2f}')

print(f'\nTotal de kWh consumido - Residencial: {total_residencial}')
print(f'Total de kWh consumido - Comercial: {total_comercial}')
print(f'Total de kWh consumido - Industrial: {total_industrial}')

if quantidade_consumidores > 0:
    kwh_total_geral = total_residencial + total_comercial + total_industrial
    media_geral = kwh_total_geral / quantidade_consumidores
    print(f'Quantidade média geral de consumo: {media_geral:.2f} kWh')
