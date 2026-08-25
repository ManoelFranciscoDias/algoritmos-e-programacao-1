salario = float(input('Informe qual é o seu salario: '))

if salario >= 0:
    if salario < 10_000:
        reajuste = 'Você teve um reajuste salarial de 55%'
        novo_salario = salario * 1.55

    elif 10_000 <= salario <= 25_000:
        reajuste = 'Você teve um reajuste de 20%'
        novo_salario = salario * 1.20

    else:
        reajuste = 'Você teve um reajuste de 20%'
        novo_salario = salario * 1.20

    print(reajuste)
    print(f'Novo salário: R$ {novo_salario:.2f}')

else:
    print('Erro! Salário Negativo')