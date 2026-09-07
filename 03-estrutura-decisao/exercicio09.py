# Exercício 9: Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e
# escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que se a nota
# for igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

if 0 <= nota_1 <= 10 and 0 <= nota_2 <= 10:
    media = (nota_1 + nota_2) / 2
    print(f'Média: {media:.2f}')
    
    if media >= 6:
        print('Você foi aprovado!')
    else:
        print('Você não foi aprovado!')
else:
    print('Digite notas válidas!')