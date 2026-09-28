# Exercício 9: Escreva uma função que receba dois números inteiros x e y. Essa
# função deve verificar se x é divisível por y. No caso positivo, a função deve
# retornar 1, caso contrário zero. Escreva também um programa para testar tal
# função.

def verificar_divisivel(x, y):
    if y == 0:
        return 0
    if x % y == 0:
        return 1
    return 0

x = int(input('Informe o valor de x: '))
y = int(input('Informe o valor de y: '))

resultado = verificar_divisivel(x, y)

if resultado == 1:
    print(f'{x} é divisível por {y}')
else:
    print(f'{x} não é divisível por {y}')