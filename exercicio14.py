"""
Faça um algoritmo que leia as medidas dos 4 lados de um terreno, o preço 
de um mourão e o preço de um metro de arame farpado. Deve ser escrito:
- o número de mourões necessários para cercar o terreno, colocando um 
mourão a cada 3 metros;
- o gasto total, o gasto em mourões e o gasto em arame, supondo que a 
cerca seja feita com 4 fios de arame.
"""
lado_1 = float(input('Informe a medida do primeiro lado do terreno: '))
lado_2 = float(input('Informe a medida do segundo lado do terreno: '))
lado_3 = float(input('Informe a medida do terceiro lado do terreno: '))
lado_4 = float(input('Informe a medida do quarto lado do terreno: '))
preco_mourao = float(input('Informe qual é o preço do mourão: '))
preco_arame_farp = float(input('Informe qual é o preço do arame farpado: '))

tamanho_terreno = lado_1 + lado_2 + lado_3 + lado_4
mourao_necessario = tamanho_terreno // 3

gastos_mourao = mourao_necessario * preco_mourao
gasto_arame = tamanho_terreno * 4 * preco_arame_farp
gasto_total = gastos_mourao + gasto_arame

print('-' * 15)
print(f'Será necessario {mourao_necessario:.0f} mourão')
print(f'O valor gasto com mourão sera de R${gastos_mourao:.2f}')
print(f'Será gasto com arame farpado R${gasto_arame:.2f}')
print(f'O gasto total será de R${gasto_total:.2f}')

