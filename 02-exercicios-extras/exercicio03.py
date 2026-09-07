# Exercício 3: Fazer um algoritmo para ler os valores da base e altura de um retângulo e mostrar seu
# perímetro (2 x (base + altura)) e sua área (base x altura).

base = float(input('Informe a base do retângulo: '))
altura = float(input('Informe a altura do retângulo: '))

perimetro = 2 * (base + altura)
area = base * altura

print('-' * 15)
print(f'Base: {base:.2f}  |  Altura: {altura:.2f}')
print(f'Perímetro: {perimetro:.2f}')
print(f'Área: {area:.2f}')