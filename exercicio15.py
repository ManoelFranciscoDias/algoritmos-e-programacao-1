modelo = input('Informe qual é o modelo do carro: ')
marca = input('Informe qual é a marca do carro: ')
ano = input('Infome qual é o ano do carro: ')
km_inicial = float(input('Informe o KM inicial do carro: '))
km_final = float(input('Informe o KM final do carro: '))
litros_consumidos = float(input('Informe a quantidade de litros de combustivel consumidos: '))
preco_por_litro = float(input('Informe o preço por litro: '))

distancia_percorrida = km_final -  km_inicial

print('-' * 15)
print(f'Modelo: {modelo}    Marca: {marca}    Ano: {ano}')
print(f'Distancia percorrida: {distancia_percorrida:.1f}KM')
print(f'Litros de conbustivel consumidos: {litros_consumidos:.1f}L')
print(f'Preço por litro: R${preco_por_litro:.2f}')
print(f'Preço a pagar: R${(preco_por_litro * litros_consumidos):.2f}')
print(f'KM por Litro: {(distancia_percorrida / litros_consumidos):.2f}')


