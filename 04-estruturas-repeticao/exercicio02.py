# Exercício 2: Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido,
# se é par ou ímpar.

contador = 1

while contador <= 15:
    numero = int(input(f'Digite o {contador}° número: '))

    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
        
    contador += 1
