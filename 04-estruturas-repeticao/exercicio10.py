# Exercício 10: Construir um algoritmo que calcule o fatorial de um número N.

n = int(input('Digite um número inteiro: '))

if n < 0:
    print('Não existe fatorial de número negativo.')
else:
    fatorial = 1

    for i in range(n, 0, -1):
        fatorial *= i

    print(f'O fatorial de {n} é {fatorial}')
