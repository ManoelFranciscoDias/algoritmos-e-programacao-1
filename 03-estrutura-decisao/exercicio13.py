# Exercício 13: Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do
# vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

nome_time_1 = input('Informe o nome do primeiro time: ')
nome_time_2 = input('Informe o nome do segundo time: ')
gols_time_1 = int(input(f'Quantos gols o {nome_time_1} marcou? '))
gols_time_2 = int(input(f'Quantos gols o {nome_time_2} marcou? '))

if gols_time_1 > gols_time_2:
    print(f'O {nome_time_1} foi o vencedor')
elif gols_time_2 > gols_time_1:
    print(f'O {nome_time_2} foi o vencedor')
else:
    print('EMPATE')
