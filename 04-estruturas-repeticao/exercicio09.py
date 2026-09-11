# Exercício 9: Faça um algoritmo que calcule e imprima os valores de y, onde:
# y = (3 + 2x + 6x²) / (1 + 9x + 16x²), para x variando de 1.0 até 5.0, em intervalos de 0.1
# unidades.

for i in range(10, 51):
    x = i / 10

    y = (3 + 2*x + 6*x**2) / (1 + 9*x + 16*x**2)

    print(f'x = {x} -> y = {y:.5f}')

