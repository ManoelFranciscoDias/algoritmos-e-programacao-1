# Exercício 3: Escreva um programa para ler as notas das duas avaliações de um
# aluno no semestre. Faça uma função que receba as duas notas por parâmetro e
# calcule e escreva a média semestral e a mensagem "PARABÉNS! Você foi aprovado!"
# somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f'Média semestral: {media:.2f}')
    if media >= 6:
        print('PARABÉNS! Você foi aprovado!')

nota1 = float(input('Digite a nota da primeira avaliação: '))
nota2 = float(input('Digite a nota da segunda avaliação: '))

calcular_media(nota1, nota2)