# Exercício 1: Ler um valor e escrever se é positivo, negativo ou zero.

valor = float(input('Insira um valor numérico: '))

if valor > 0:
    print('Valor positivo')
elif valor < 0:
    print('Valor negativo')
else:
    print('Esse valor é 0')