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
print(f'Serão necessários {mourao_necessario:.0f} mourões')
print(f'O valor gasto com mourões será de R${gastos_mourao:.2f}')
print(f'Será gasto com arame farpado R${gasto_arame:.2f}')
print(f'O gasto total será de R${gasto_total:.2f}')