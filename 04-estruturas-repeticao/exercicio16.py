# Exercício 16: Fazer um algoritmo que calcule e imprima o valor de e^x através da série:
# e^x = x^0 + x^1/1! + x^2/2! + x^3/3! + ...
# Considerar para efeitos de cálculo os 30 primeiros termos. O algoritmo deverá ler o valor de x.
import math

x = float(input('Informe o valor de x: '))
soma = 0

for i in range(0, 30):
    termo = x**i / math.factorial(i)
    soma += termo

print(f'O valor de e^{x} é {soma:.2f}')
