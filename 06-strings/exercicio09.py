# Exercício 9 (Verificação de CPF): Desenvolva um programa que solicite a digitação de um número
# de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da
# validação dos dígitos verificadores e dos caracteres de formatação.

cpf = input('Digite o CPF (xxx.xxx.xxx-xx): ')

formato_valido = len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'
numeros = cpf.replace('.', '').replace('-', '')

if not formato_valido or len(numeros) != 11 or not numeros.isdecimal():
    print('CPF inválido: o formato deve ser xxx.xxx.xxx-xx.')
elif numeros == numeros[0] * 11:
    print('CPF inválido: todos os dígitos são iguais.')
else:
    soma = 0
    for i in range(9):
        soma += int(numeros[i]) * (10 - i)
    digito_1 = (soma * 10) % 11 % 10

    soma = 0
    for i in range(10):
        soma += int(numeros[i]) * (11 - i)
    digito_2 = (soma * 10) % 11 % 10

    if digito_1 == int(numeros[9]) and digito_2 == int(numeros[10]):
        print('CPF válido.')
    else:
        print('CPF inválido: os dígitos verificadores não conferem.')
