# Exercício 21: Uma turma tem 50 alunos. Faça um algoritmo que:
# - leia para cada aluno o seu nome e idade;
# - escreva os nomes dos alunos que tem 18 anos;
# - escreva a quantidade de alunos que tem idade acima de 20 anos.

acima_de_20 = 0
com_18_anos = []

for i in range(1, 51):
    nome = input(f'Informe o nome do {i}° aluno: ')
    idade = int(input(f'Informe a idade de {nome}: '))

    if idade == 18:
        com_18_anos.append(nome)

    if idade > 20:
        acima_de_20 += 1


if com_18_anos:
    print(f'Os alunos que têm 18 anos são: {", ".join(com_18_anos)}')
else:
    print('Nenhum aluno tem 18 anos.')

print(f'{acima_de_20} aluno(s) tem idade acima dos 20 anos')

