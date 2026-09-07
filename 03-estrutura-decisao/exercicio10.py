# Exercício 10: Escrever um algoritmo para ler duas notas de um aluno e escrever na tela a palavra
# "Aprovado" se a média das duas notas for maior ou igual a 7,0. Caso a média seja
# inferior a 7,0, o programa deve ler a nota do exame e calcular a média final. Se esta
# média for maior ou igual a 5,0, o programa deve escrever "Aprovado", caso contrário deve
# escrever "Reprovado".

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

if 0 <= nota_1 <= 10 and 0 <= nota_2 <= 10:
    media = (nota_1 + nota_2) / 2

    if media >= 7:
        print('Aprovado')
    else:
        exame = float(input('Digite sua nota do exame: '))
        if 0 <= exame <= 10:
            media_com_exame = (nota_1 + nota_2 + exame) / 3
            if media_com_exame >= 5:
                print('Aprovado')
            else:
                print('Reprovado')
        else:
            print('Nota do exame inválida')
else:
    print('Digite notas válidas')