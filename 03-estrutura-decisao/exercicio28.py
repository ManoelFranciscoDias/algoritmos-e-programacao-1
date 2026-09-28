# Exercício 28: Uma empresa decidiu conceder um aumento de salário a seus funcionários de acordo com a
# tabela: salário <= 400.00 = 15%; 400.00 < salário <= 700.00 = 12%; 700.00 < salário <=
# 1000.00 = 10%; 1000.00 < salário <= 1500.00 = 7%; 1500.00 < salário <= 2000.00 = 4%;
# salário > 2000.00 = sem aumento. Faça um algoritmo que leia o salário atual de um
# funcionário e escreva o índice de aumento e o valor do salário corrigido.

salario = float(input('Informe o seu salário: '))

if salario < 0:
    print('Erro! O salário não pode ser negativo.')
else:
    if salario <= 400:
        percentual_aumento = 15
    elif salario <= 700:
        percentual_aumento = 12
    elif salario <= 1000:
        percentual_aumento = 10
    elif salario <= 1500:
        percentual_aumento = 7
    elif salario <= 2000:
        percentual_aumento = 4
    else:
        percentual_aumento = 0

    salario_corrigido = salario * (1 + percentual_aumento / 100)

    if percentual_aumento > 0:
        print(f'Índice de aumento: {percentual_aumento}%')
    else:
        print('Sem aumento')
    print(f'Salário corrigido: R$ {salario_corrigido:.2f}')
