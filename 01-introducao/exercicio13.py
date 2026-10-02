# Exercício 13: Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto
# vai gastar para fazer uma viagem até a casa de sua irmã. Faça um algoritmo que leia: a
# distância da casa de Maria até sua irmã; o consumo do carro de Maria (KM rodados / litro); o
# preço da gasolina (litro). E mostre as informações que Maria necessita.

distancia = float(input('Informe a distância (em km) da casa de Maria até a casa da irmã: '))
consumo_carro = float(input('Informe o consumo do carro (km/L): '))
preco_gasolina = float(input('Informe o preço do litro da gasolina: '))

if consumo_carro <= 0:
    print('Erro! O consumo do carro deve ser maior que zero.')
else:
    litros_necessarios = distancia / consumo_carro
    custo_viagem = litros_necessarios * preco_gasolina

    print(f'Maria vai precisar de {litros_necessarios:.2f} L de gasolina',
          'para chegar à casa da irmã')
    print(f'Maria vai gastar R$ {custo_viagem:.2f}')
