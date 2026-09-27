# Exercício 4: Faça um programa que leia a altura e o sexo (codificado da
# seguinte forma: 1-feminino 2-masculino) de uma pessoa. Depois faça uma função
# chamada pesoideal que receba a altura e o sexo via parâmetro e que calcule e
# retorne seu peso ideal, utilizando as seguintes fórmulas:
# - para homens: (72.7 * h) - 58
# - para mulheres: (62.1 * h) - 44.7
# Observação: Altura = h (na fórmula acima).

def pesoideal(altura, sexo):
    if sexo == 1:
        return (62.1 * altura) - 44.7
    else:
        return (72.7 * altura) - 58


sexo = int(input('Informe o seu sexo (1-feminino 2-masculino): '))
altura = float(input('Informe qual é a sua altura (em metros): '))

if sexo == 1 or sexo == 2:
    peso = pesoideal(altura, sexo)
    print(f'O seu peso ideal é: {peso:.2f} kg')
else:
    print('Sexo inválido! Digite 1 para feminino ou 2 para masculino.')