# Exercício 3: Calcule a soma de dois números, se o resultado for maior que 10, mostre-o na tela.

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))

soma = numero_1 + numero_2

if soma > 10:
    print(f'A soma é: {soma}')