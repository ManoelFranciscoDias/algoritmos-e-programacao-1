# Exercício 11: Escrever um algoritmo para ler a quantidade de horas aula dadas por dois
# professores e o valor por hora recebido por cada um. Mostrar na tela qual dos professores tem
# salário total maior.

nome_professor_1 = input('Qual o nome do primeiro professor? ')
nome_professor_2 = input('Qual o nome do segundo professor? ')
horas_professor_1 = float(input(f'Quantas horas-aula o professor {nome_professor_1} deu? '))
horas_professor_2 = float(input(f'Quantas horas-aula o professor {nome_professor_2} deu? '))
pergunta = f'Qual o valor da hora-aula do professor {nome_professor_1}? '
valor_hora_professor_1 = float(input(pergunta))
pergunta = f'Qual o valor da hora-aula do professor {nome_professor_2}? '
valor_hora_professor_2 = float(input(pergunta))

salario_professor_1 = horas_professor_1 * valor_hora_professor_1
salario_professor_2 = horas_professor_2 * valor_hora_professor_2

print('-' * 15)
print(f'Salário {nome_professor_1}: R$ {salario_professor_1:.2f}')
print(f'Salário {nome_professor_2}: R$ {salario_professor_2:.2f}')

if salario_professor_1 > salario_professor_2:
    print(f'O professor {nome_professor_1} tem um salário maior')
elif salario_professor_2 > salario_professor_1:
    print(f'O professor {nome_professor_2} tem um salário maior')
else:
    print('Os salários são iguais')
