# Exercício 34: Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica:
# se dividirmos o número em dois números de dois dígitos, um composto pela dezena e pela
# unidade, e outro pelo milhar e pela centena, e, ao somarmos estes dois novos números
# gerando um terceiro, o quadrado deste terceiro número é exatamente o número original de
# quatro dígitos. Exemplo: 2025 -> dividindo: 20 e 25 -> somando temos 45 -> 45^2 = 2025.
# Escreva um programa para ler um número e verificar se ele obedece a esta característica.

numero = int(input('Digite um número de 4 dígitos (entre 1000 e 9999): '))

if numero >= 1000 and numero <= 9999:
    parte1 = numero // 100
    parte2 = numero % 100
    soma = parte1 + parte2
    quadrado = soma ** 2

    if quadrado == numero:
        print(f'{numero} obedece à característica! ({parte1} + {parte2} = {soma}, e {soma}² = {quadrado})')
    else:
        print(f'{numero} NÃO obedece à característica. ({parte1} + {parte2} = {soma}, mas {soma}² = {quadrado})')
else:
    print('O número precisa estar entre 1000 e 9999.')