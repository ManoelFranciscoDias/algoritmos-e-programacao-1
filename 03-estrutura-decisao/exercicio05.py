# Exercício 5: Construir um algoritmo que indique se o número digitado está entre 20 e 90 ou não.

numero = float(input('Digite um número: '))

if 20 <= numero <= 90:
    print(f'O número {numero} está entre 20 e 90')
else:
    print(f'O número {numero} não está entre 20 e 90')