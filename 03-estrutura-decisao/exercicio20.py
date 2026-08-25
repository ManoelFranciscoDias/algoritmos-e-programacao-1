valor_1 = float(input('Digite o primeiro valor: '))
valor_2 = float(input('Digite o segundo valor: '))
valor_3 = float(input('Digite o terceiro valor: '))

if valor_1 > valor_2 and valor_1 > valor_3:
    print(f'O valor {valor_1} é o valor maior')
elif valor_2 > valor_1 and valor_2 > valor_3:
    print(f'O valor {valor_2} é o valor maior')
else:
    print(f'O valor {valor_3} é o valor maior')