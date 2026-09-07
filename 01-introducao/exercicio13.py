# Exercício 13: Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai
# gastar para fazer uma viagem até a casa de sua irmã. Faça um algoritmo que leia: a
# distância da casa de Maria até sua irmã; o consumo do carro de Maria (KM rodados /
# litro); o preço da gasolina (litro). E mostre as informações que Maria necessita.

distancia_casa = float(input('Informe qual é a distância da casa de Maria até sua irmã? '))
consumo_carro = float(input('Informe o consumo do carro (KM/L): '))
preco_gasolina = float(input('Informe o preço da gasolina (litro): '))

litros_necessarios = distancia_casa / consumo_carro
valor_gasto = litros_necessarios * preco_gasolina

print(f'Maria vai precisar de {litros_necessarios:.2f}L para chegar até a casa de sua irmã')
print(f'Maria vai ter um gasto de R${valor_gasto:.2f}')