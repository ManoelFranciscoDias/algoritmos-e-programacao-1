# Exercício 24: Escrever um algoritmo para ler dois valores e uma das seguintes operações a serem
# executadas (codificadas da seguinte forma: 1 - Adição, 2 - Subtração, 3 - Multiplicação
# e 4 - Divisão). Calcular e escrever o resultado dessa operação sobre os dois valores
# lidos.

valor_1 = float(input('Digite o primeiro valor: '))
valor_2 = float(input('Digite o segundo valor: '))

print('-' * 15)
print('1 – Adição')
print('2 – Subtração')
print('3 – Multiplicação')
print('4 – Divisão')
operacao = input('Digite o número da operação que quer realizar: ')

print('-' * 15)
if operacao == '1':
    print(f'Adição: {valor_1} + {valor_2} = {valor_1 + valor_2}')
elif operacao == '2':
    print(f'Subtração: {valor_1} - {valor_2} = {valor_1 - valor_2}')
elif operacao == '3':
    print(f'Multiplicação: {valor_1} x {valor_2} = {valor_1 * valor_2}')
elif operacao == '4':
    if valor_2 != 0:
        print(f'Divisão: {valor_1} ÷ {valor_2} = {valor_1 / valor_2}')
    else:
        print('Erro! Não é possível dividir por zero.')
else:
    print('Erro! Operação inválida.')