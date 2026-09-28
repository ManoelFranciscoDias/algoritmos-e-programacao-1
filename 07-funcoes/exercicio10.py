# Exercício 10: Criar uma função que calcule e retorne o MAIOR entre dois
# valores recebidos como parâmetros. Um programa para testar tal função deve
# ser criado.

def maior_valor(a, b):
    if a > b:
        return a
    return b


numero_1 = float(input('Informe o primeiro número: '))
numero_2 = float(input('Informe o segundo número: '))

if numero_1 == numero_2:
    print(f'Os números são iguais ({numero_1})')
else:
    print(f'O maior número é {maior_valor(numero_1, numero_2)}')
