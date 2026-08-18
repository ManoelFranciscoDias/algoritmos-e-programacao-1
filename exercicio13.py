distancia_casa = float(input('Informe qual é a distancia da casa da Maria até sua irma? '))
consumo_carro = float(input('Informe o consumo do carro (KM/L): '))
preco_gasolina = float(input('Informe o preço da gasolina (litro): '))

litros_necessarios = distancia_casa / consumo_carro
valor_gasto = litros_necessarios * preco_gasolina

print(f'Maria vai precisar de {litros_necessarios:.2f}L para chegar até a casa de sua irmã')
print(f'Maria vai ter um gasto de R${valor_gasto:.2f}')