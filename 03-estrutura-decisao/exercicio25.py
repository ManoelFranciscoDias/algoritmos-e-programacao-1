# Exercício 25: Faça um algoritmo para calcular as raízes reais de uma equação quadrática: ax^2 + bx + c
# = 0. Uma equação quadrática só tem raízes reais se (b^2 - 4ac) for maior ou igual a
# zero. Se o delta calculado for negativo, a equação não possui raízes reais (informe e
# encerre); se for igual a zero, a equação possui apenas uma raiz real (informe-a); se for
# positivo, a equação possui duas raízes reais (informe-as).

import math
print("Forma: ax² + bx + c = 0")
a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

delta = (b**2) - (4*a*c)

if delta < 0:
    print('A equação não possui raízes reais')
elif delta == 0:
    x = -b / (2 * a)
    print('A equação possui apenas uma raiz real')
    print(f'x = {x}')
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('A equação possui duas raízes reais')
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')