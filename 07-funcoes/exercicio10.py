# Exercício 10: Criar uma função que calcule e retorne o MAIOR entre dois
# valores recebidos como parâmetros. Um programa para testar tal função deve
# ser criado.

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

maior = maior_numero(num1, num2)

if num1 == num2:
    print(f'Os números são iguais ({num1})')
else:
    print(f'O maior número é {maior}')