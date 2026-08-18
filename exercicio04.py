import math
raio = float(input('Digite o valor do raio da lata de oléo: '))
altura = float(input('Digite o valor da altura da lata de oléo: '))

volume = math.pi * raio**2 * altura

print(f'O volume da lata de oléo é {volume:.2f}L')