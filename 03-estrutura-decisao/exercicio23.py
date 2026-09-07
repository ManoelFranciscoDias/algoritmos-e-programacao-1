# Exercício 23: Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. Atribuição de conceitos: entre 9.0 e
# 10.0 = A; entre 7.5 e 9.0 = B; entre 6.0 e 7.5 = C; entre 4.0 e 6.0 = D; entre 4.0 e
# zero = E. O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
# e a mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o conceito for D
# ou E.

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