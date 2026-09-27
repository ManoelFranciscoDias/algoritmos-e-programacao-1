# Exercício 8: Escreva uma função que receba um número natural e imprima os
# três primeiros caracteres do dia da semana correspondente ao número. Por
# exemplo, 7 corresponde a "SAB". O procedimento deve mostrar uma mensagem de
# erro caso o número recebido não corresponda a um dia da semana. Gere também
# um programa que utilize essa função, chamando-a, mas antes lendo um valor
# para passagem de parâmetro.

def dia_semana(numero):
    dias = ['DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']
    if 1 <= numero <= 7:
        print(dias[numero - 1])
    else:
        print('Erro: o número deve estar entre 1 e 7.')


n = int(input('Digite o número do dia da semana (1 a 7): '))
dia_semana(n)