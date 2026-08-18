a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
d = float(input('Digite o valor de D: '))
e = float(input('Digite o valor de E: '))
f = float(input('Digite o valor de F: '))

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print(f'O valores de x e y são {x:.2f} e {y:.2f} respectivamente')