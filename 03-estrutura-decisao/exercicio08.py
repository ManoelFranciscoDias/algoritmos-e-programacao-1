idade = int(input('Digite a sua idade: '))

if idade < 0:
    print('Inválido!')
elif idade <= 17:
    print('Menor de idade')
elif idade <= 65:
    print('Maior de idade')
else:
    print('Acima de 65 anos')