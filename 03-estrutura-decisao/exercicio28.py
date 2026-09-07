# Exercício 28: Uma empresa decidiu conceder um aumento de salário a seus funcionários de acordo com a
# tabela: salário <= 400.00 = 15%; 400.00 < salário <= 700.00 = 12%; 700.00 < salário <=
# 1000.00 = 10%; 1000.00 < salário <= 1500.00 = 7%; 1500.00 < salário <= 2000.00 = 4%;
# salário > 2000.00 = sem aumento. Faça um algoritmo que leia o salário atual de um
# funcionário e escreva o índice de aumento e o valor do salário corrigido.

salario = float(input('Informe qual é o seu salário: '))

if salario >= 0:
    if salario <= 400:
        print('Índice de Aumento: 15%')
        print(f'Salário corrigido: R${(salario * 1.15):.2f}')
    elif 400 < salario <= 700:
        print('Índice de Aumento: 12%')
        print(f'Salário corrigido: R${(salario * 1.12):.2f}')
    elif 700 < salario <= 1000:
        print('Índice de Aumento: 10%')
        print(f'Salário corrigido: R${(salario * 1.10):.2f}')
    elif 1000 < salario <= 1500:
        print('Índice de Aumento: 7%')
        print(f'Salário corrigido: R${(salario * 1.07):.2f}')
    elif 1500 < salario <= 2000:
        print('Índice de Aumento: 4%')
        print(f'Salário corrigido: R${(salario * 1.04):.2f}')
    else:
        print('Sem aumento')
        print(f'Salário: R${salario:.2f}')
else:
    print('Erro! Salário Negativo')