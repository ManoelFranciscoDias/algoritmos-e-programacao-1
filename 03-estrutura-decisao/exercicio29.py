# Exercício 29: Faça um algoritmo para calcular o reajuste salarial de um funcionário: se salário é
# inferior a R$ 10.000,00, reajuste de 55%; se está entre R$ 10.000,00 (inclusive) e R$
# 25.000,00 (inclusive), reajuste de 20%; se é superior a R$ 25.000,00, reajuste de 20%.

salario = float(input('Informe o seu salário: '))

if salario < 0:
    print('Erro! O salário não pode ser negativo.')
else:
    if salario < 10_000:
        percentual_reajuste = 55
    elif salario <= 25_000:
        percentual_reajuste = 20
    else:
        percentual_reajuste = 20

    novo_salario = salario * (1 + percentual_reajuste / 100)

    print(f'Você teve um reajuste salarial de {percentual_reajuste}%')
    print(f'Novo salário: R$ {novo_salario:.2f}')
