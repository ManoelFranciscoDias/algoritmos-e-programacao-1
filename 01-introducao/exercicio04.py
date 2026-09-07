# Exercício 4: Faça um algoritmo que calcule o volume de uma lata de óleo. Escreva o resultado.
# FÓRMULA: volume = pi * raio^2 * altura

import math

raio = float(input('Digite o valor do raio da lata de óleo: '))
altura = float(input('Digite o valor da altura da lata de óleo: '))

volume = math.pi * raio**2 * altura

print(f'O volume da lata de óleo é {volume:.2f}')