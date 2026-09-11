# Exercício 10: Construir um algoritmo que calcule o fatorial de um número N.
n = int(input('Digite um número inteiro: '))

fatorial = 1

for i in range(n, 0, -1):
    fatorial *= i

print(f'O fatorial de 4 é {fatorial}')