# Exercício 6: Faça um algoritmo que leia n valores inteiros e escreva quantos desses valores
# são negativos.

n = int(input('Quantos valores inteiros deseja digitar? '))
contador = 1
quantidade_negativos = 0

while contador <= n:
    numero = int(input(f'Digite o {contador}º valor: '))
    if numero < 0:
        quantidade_negativos += 1

    contador += 1

print(f'Quantidade de números negativos: {quantidade_negativos}')
