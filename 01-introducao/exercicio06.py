import math

x1 = float(input('Informe a coordenada x1: '))
y1 = float(input('Informe a coordenada y1: '))
x2 = float(input('Informe a coordenada x2: '))
y2 = float(input('Informe a coordenada y2: '))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f'A distância entre os pontos é {distancia:.2f}')