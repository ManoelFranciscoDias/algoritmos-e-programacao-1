# Exercício 2: Faça uma função que calcule a hipotenusa. Os catetos são os dados
# de entrada e a hipotenusa é o dado de saída.
#
# hipotenusa = sqrt(catetoA² + catetoB²)

import math


def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)


cateto_a = float(input('Digite o valor do cateto A: '))
cateto_b = float(input('Digite o valor do cateto B: '))

hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

print(f'A hipotenusa é {hipotenusa:.2f}')
