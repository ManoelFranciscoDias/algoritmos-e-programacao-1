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