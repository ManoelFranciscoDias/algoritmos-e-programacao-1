# Exercício 10 (Número por extenso): Escreva um programa que solicite ao usuário a digitação de
# um número até 99 e imprima-o na tela por extenso.

unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
            'dezoito', 'dezenove']

dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta',
           'oitenta', 'noventa']

numero = int(input('Digite um número de 0 a 99: '))

if numero < 0 or numero > 99:
    print('Número inválido. Digite um número de 0 a 99.')
elif numero < 20:
    print(unidades[numero])
elif numero % 10 == 0:
    print(dezenas[numero // 10])
else:
    print(f'{dezenas[numero // 10]} e {unidades[numero % 10]}')
