nome_time_1 = input('Informe o nome do primeiro time: ')
nome_time_2 = input('Informe o nome do segundo time: ')
gol_time_1 = int(input(f'Quantos gol o {nome_time_1} marcou: '))
gol_time_2 = int(input(f'Quantos gol o {nome_time_2} marcou: '))

if gol_time_1 > gol_time_2:
    print(f'O {nome_time_1} foi o vencedor')
elif gol_time_2 > gol_time_1:
    print(f'O {nome_time_2} foi o vencedor')
else:
    print('EMPATE')