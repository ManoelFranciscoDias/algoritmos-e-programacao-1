base = float(input('Informe a base do retângulo: '))
altura = float(input('Informe a altura do retângulo: '))

perimetro = 2 * (base + altura)
area = base * altura

print('-' * 15)
print(f'Base: {base:.2f}  |  Altura: {altura:.2f}')
print(f'Perímetro: {perimetro:.2f}')
print(f'Área: {area:.2f}')