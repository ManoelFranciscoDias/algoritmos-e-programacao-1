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