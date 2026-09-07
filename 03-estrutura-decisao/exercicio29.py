# Exercício 29: Faça um algoritmo para calcular o reajuste salarial de um funcionário: se salário é
# inferior a R$ 10.000,00, reajuste de 55%; se está entre R$ 10.000,00 (inclusive) e R$
# 25.000,00 (inclusive), reajuste de 20%; se é superior a R$ 25.000,00, reajuste de 20%.

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