# Exercício 7: Construir um algoritmo para ler o raio de uma circunferência e mostrar o perímetro (2 x
# pi x raio) e a área (pi x raio^2). Utilize o pi como constante.

import math
raio = float(input('Informe o raio de uma circunferência: '))

perimetro = 2 * math.pi * raio
area = math.pi * raio**2

print(f'O perímetro da circunferência é de {perimetro:.2f}')
print(f'A área da circunferência é de {area:.2f}')