# Exercício 7: Escreva uma função que receba um número inteiro e imprima o mês
# correspondente ao número. Por exemplo, 2 corresponde a "fevereiro". O
# procedimento deve mostrar uma mensagem de erro caso o número recebido não
# faça sentido. Gere também um programa que leia um valor e chame a função
# criada.

def exibir_mes(numero):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    if 1 <= numero <= 12:
        print(meses[numero - 1])
    else:
        print('Erro: o número deve estar entre 1 e 12.')


numero_mes = int(input('Digite o número do mês (1 a 12): '))
exibir_mes(numero_mes)
