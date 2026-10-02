# Exercício 22: Faça um algoritmo que:
# - leia, para n pessoas, a altura e o sexo (sexo = 'M' ou sexo = 'm' para masculino e
#   sexo = 'F' ou sexo = 'f' para feminino);
# - escreva a média da altura das mulheres;
# - escreva a média da altura da turma.

n = int(input('Quantas pessoas deseja cadastrar? '))

soma_alturas_mulheres = 0
quantidade_mulheres = 0
soma_alturas_turma = 0

for i in range(1, n + 1):
    pergunta = f'Digite o sexo da {i}ª pessoa (M para masculino, F para feminino): '
    sexo = input(pergunta).strip().upper()

    while sexo != 'M' and sexo != 'F':
        print('Sexo inválido! Digite M ou F.')
        sexo = input(pergunta).strip().upper()

    altura = float(input(f'Digite a altura da {i}ª pessoa: '))

    soma_alturas_turma += altura
    if sexo == 'F':
        soma_alturas_mulheres += altura
        quantidade_mulheres += 1

if quantidade_mulheres > 0:
    media_altura_mulheres = soma_alturas_mulheres / quantidade_mulheres
    print(f'A média da altura das mulheres é {media_altura_mulheres:.2f}')
else:
    print('Nenhuma mulher foi cadastrada.')

if n > 0:
    media_altura_turma = soma_alturas_turma / n
    print(f'A média da altura da turma é {media_altura_turma:.2f}')
else:
    print('Nenhuma pessoa foi cadastrada.')
