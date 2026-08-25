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