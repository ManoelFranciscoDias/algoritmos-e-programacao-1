nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))

if 0 <= nota_1 <= 10 and 0 <= nota_2 <= 10:
    media = (nota_1 + nota_2) / 2

    print('-' * 15)
    print(f'Notas: {nota_1}, {nota_2}')
    print(f'Média: {media}')

    if 9 <= media <= 10:
        conceito = 'A'
        situacao = 'Aprovado'
    elif 7.5 <= media < 9:
        conceito = 'B'
        situacao = 'Aprovado'
    elif 6 <= media < 7.5:
        conceito = 'C'
        situacao = 'Aprovado'
    elif 4 <= media < 6:
        conceito = 'D'
        situacao ='Reprovado'
    else:
        conceito = 'E'
        situacao = 'Reprovado'

    print(f'Conceito: {conceito}')
    print(situacao)
else:
    print('Digite notas entre 0 e 10')