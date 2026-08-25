numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
else:
    print('Erro: você precisa digitar um número inteiro válido!')