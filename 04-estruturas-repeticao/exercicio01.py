# Exercício 1: Faça um algoritmo que:
# - leia 20 números inteiros;
# - escreva os números que são negativos;
# - escreva a média dos números positivos.

contador = 1
soma_positivos = 0
quantidade_positivos = 0
negativos = []

while contador <= 20:
    numero = int(input(f'Digite o {contador}º número: '))
    if numero < 0:
        negativos.append(numero)
    elif numero > 0:
        soma_positivos += numero
        quantidade_positivos += 1

    contador += 1

if negativos:
    print(f'Números negativos: {negativos}')
else:
    print('Nenhum número negativo foi digitado.')
if quantidade_positivos > 0:
    print(f'A média dos números positivos é {(soma_positivos / quantidade_positivos):.2f}')
else:
    print('Não há números positivos para calcular a média.')
