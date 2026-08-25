nome_professor_1 = input('Qual o nome do primeiro professor? ')
nome_professor_2 = input('Qual o nome do segundo professor? ')
aulas_professor_1 = float(input(f'Qual a quantidade de horas aula dadas pelo professor {nome_professor_1}? '))
aulas_professor_2 = float(input(f'Qual a quantidade de horas aula dadas pelo professor {nome_professor_2}? '))
hora_professor_1 = float(input(f'Qual o valor por hora recebido do professor {nome_professor_1}? '))
hora_professor_2 = float(input(f'Qual o valor por hora recebido do professor {nome_professor_2}? '))

salario_professor_1 = aulas_professor_1 * hora_professor_1
salario_professor_2 = aulas_professor_2 * hora_professor_2

print('-' * 15)
print(f'Salário {nome_professor_1}:     R${salario_professor_1:.2f}')
print(f'Salário {nome_professor_2}:     R${salario_professor_2:.2f}')

if salario_professor_1 > salario_professor_2:
    print(f'O professor {nome_professor_1} tem um salário maior')
elif salario_professor_2 > salario_professor_1:
    print(f'O professor {nome_professor_2} tem um salário maior')
else:
    print('Os salários são iguais')