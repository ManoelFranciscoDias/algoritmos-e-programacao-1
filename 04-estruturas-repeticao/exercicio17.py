# Exercício 17: Foi feita uma pesquisa de audiência de canal de TV em n casas de um determinado
# bairro de Joinville, em um certo dia do mês. Na pesquisa foi utilizado um coletor de dados
# portátil. Para cada casa visitada, foi fornecido o número do canal (4, 5, 9, 12) e o número de
# pessoas que estavam assistindo a TV naquele horário, considerando que em cada casa só existia
# uma televisão. Em casas onde a televisão estava desligada, foi registrado zero para o número do
# canal e para o número de pessoas. Faça um algoritmo que calcule e escreva, para cada emissora,
# o percentual de audiência.

casas = int(input('Digite quantas casas foram feita as pesquisas: '))

soma_canal_4 = 0
soma_canal_5 = 0
soma_canal_9 = 0
soma_canal_12 = 0
soma_desligada = 0

for i in range(1, casas + 1):
    canal = int(input(f'Na casa {i}, qual foi o canal assistido? (0 = desligada, 4, 5, 9, 12): '))

    if canal == 0:
        pessoas = 0
        soma_desligada += 1
    elif canal in (4, 5, 9, 12):
        pessoas = int(input(f'Na casa {i}, quantas pessoas estavam assistindo TV? '))
        if canal == 4:
            soma_canal_4 += pessoas
        elif canal == 5:
            soma_canal_5 += pessoas
        elif canal == 9:
            soma_canal_9 += pessoas
        else:
            soma_canal_12 += pessoas
    else:
        print('Canal inválido! Digite 0, 4, 5, 9 ou 12.')

total_pessoas = soma_canal_4 + soma_canal_5 + soma_canal_9 + soma_canal_12

if total_pessoas > 0:
    porcentagem_canal_4 = (soma_canal_4 / total_pessoas) * 100
    porcentagem_canal_5 = (soma_canal_5 / total_pessoas) * 100
    porcentagem_canal_9 = (soma_canal_9 / total_pessoas) * 100
    porcentagem_canal_12 = (soma_canal_12 / total_pessoas) * 100

else:
    porcentagem_canal_4 = porcentagem_canal_5 = porcentagem_canal_9 = porcentagem_canal_12 = 0

print(f'\nCasas com TV desligada: {soma_desligada}')
print(f'Canal 4: {porcentagem_canal_4:.2f}%')
print(f'Canal 5: {porcentagem_canal_5:.2f}%')
print(f'Canal 9: {porcentagem_canal_9:.2f}%')
print(f'Canal 12: {porcentagem_canal_12:.2f}%')