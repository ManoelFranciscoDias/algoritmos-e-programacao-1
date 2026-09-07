# Exercício 15: São dados de entrada sobre um automóvel: modelo, marca, ano, km inicial, km final,
# litros de combustível consumidos, preço por litro. Faça um algoritmo que escreva os
# dados de saída: modelo, marca, ano, distância percorrida, litros de combustível
# consumidos, preço por litro, total a pagar e km por litro.

modelo = input('Informe qual é o modelo do carro: ')
marca = input('Informe qual é a marca do carro: ')
ano = input('Informe qual é o ano do carro: ')
km_inicial = float(input('Informe o KM inicial do carro: '))
km_final = float(input('Informe o KM final do carro: '))
litros_consumidos = float(input('Informe a quantidade de litros de combustível consumidos: '))
preco_por_litro = float(input('Informe o preço por litro: '))

distancia_percorrida = km_final - km_inicial
total_a_pagar = preco_por_litro * litros_consumidos
km_por_litro = distancia_percorrida / litros_consumidos

print('-' * 15)
print(f'Modelo: {modelo}    Marca: {marca}    Ano: {ano}')
print(f'Distância percorrida: {distancia_percorrida:.1f}KM')
print(f'Litros de combustível consumidos: {litros_consumidos:.1f}L')
print(f'Preço por litro: R${preco_por_litro:.2f}')
print(f'Preço a pagar: R${total_a_pagar:.2f}')
print(f'KM por Litro: {km_por_litro:.2f}')