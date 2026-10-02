# Exercício 14: Faça um algoritmo que leia as medidas dos 4 lados de um terreno, o preço de um
# mourão e o preço de um metro de arame farpado. Deve ser escrito: o número de mourões
# necessários para cercar o terreno, colocando um mourão a cada 3 metros; o gasto total, o gasto
# em mourões e o gasto em arame, supondo que a cerca seja feita com 4 fios de arame.

import math

lado_1 = float(input('Informe a medida do primeiro lado do terreno (em metros): '))
lado_2 = float(input('Informe a medida do segundo lado do terreno (em metros): '))
lado_3 = float(input('Informe a medida do terceiro lado do terreno (em metros): '))
lado_4 = float(input('Informe a medida do quarto lado do terreno (em metros): '))
preco_mourao = float(input('Informe o preço de um mourão: '))
preco_metro_arame = float(input('Informe o preço do metro de arame farpado: '))

perimetro_terreno = lado_1 + lado_2 + lado_3 + lado_4
quantidade_mouroes = math.ceil(perimetro_terreno / 3)

gasto_mouroes = quantidade_mouroes * preco_mourao
gasto_arame = perimetro_terreno * 4 * preco_metro_arame
gasto_total = gasto_mouroes + gasto_arame

print('-' * 15)
print(f'Serão necessários {quantidade_mouroes} mourões')
print(f'O gasto com mourões será de R$ {gasto_mouroes:.2f}')
print(f'O gasto com arame farpado será de R$ {gasto_arame:.2f}')
print(f'O gasto total será de R$ {gasto_total:.2f}')
