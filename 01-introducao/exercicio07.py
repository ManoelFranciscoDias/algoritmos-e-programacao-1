# Exercício 7: Um sistema de equações lineares da forma ax + by = c, dx + ey = f pode ser resolvido com
# x = (ce - bf) / (ae - bd) e y = (af - cd) / (ae - bd). Faça um algoritmo que leia os
# valores a, b, c, d, e, f, e calcule x e y.

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
d = float(input('Digite o valor de D: '))
e = float(input('Digite o valor de E: '))
f = float(input('Digite o valor de F: '))

denominador = a * e - b * d

x = (c * e - b * f) / denominador
y = (a * f - c * d) / denominador

print(f'Os valores de x e y são {x:.2f} e {y:.2f}, respectivamente')