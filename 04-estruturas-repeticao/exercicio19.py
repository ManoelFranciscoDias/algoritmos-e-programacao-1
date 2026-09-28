# Exercício 19: Faça um algoritmo que leia n números inteiros e escreva, para cada número lido,
# os divisores e quantidade de divisores.
# EXEMPLO: número lido = 12
#          divisores = 1, 2, 3, 4, 6, 12
#          quantidade divisores = 6

n = int(input('Quantos números você vai digitar? '))

for _ in range(n):
    numero = int(input('Digite um número inteiro: '))
    divisores = []

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            divisores.append(divisor)

    print(f'Divisores de {numero}: {", ".join(str(divisor) for divisor in divisores)}')
    print(f'Quantidade de divisores: {len(divisores)}')
    print()
