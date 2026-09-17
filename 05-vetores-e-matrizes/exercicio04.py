# Exercício 4: Faça um algoritmo que leia um vetor que contém as notas de 30 alunos. Imprima o
# maior valor, o menor valor, a média da turma e a quantidade de notas abaixo da média.

lista_notas = []
notas_abaixo_da_media = []

for indice in range(30):
    nota_atual = float(input(f'Digite a nota do aluno {indice+1}: '))

    while nota_atual < 0 or nota_atual > 10:
        print('Digite uma nota entre 0 e 10')
        nota_atual = float(input(f'Digite a nota do aluno {indice+1}: '))

    lista_notas.append(nota_atual)

    if indice == 0:
        nota_maxima = nota_atual
        nota_minima = nota_atual
    else:
        if nota_atual > nota_maxima:
            nota_maxima = nota_atual
        if nota_atual < nota_minima:
            nota_minima = nota_atual

media_turma = sum(lista_notas) / len(lista_notas)

for nota in lista_notas:
    if nota < media_turma:
        notas_abaixo_da_media.append(nota)

print(f'A maior nota da turma é {nota_maxima}')
print(f'A menor nota da turma é {nota_minima}')
print(f'A média da turma é {media_turma:.2f}')
print(f'Quantidade de notas abaixo da média: {len(notas_abaixo_da_media)}')