# Exercício 28: Em uma disputa de pingue-pongue os pontos são anotados como D, ponto para o
# jogador do lado direito, e E, ponto para o jogador do lado esquerdo da mesa. Faça um algoritmo
# que leia o código do ponto de cada jogada e determine o vencedor. A partida encerra quando:
# a) um dos jogadores chegar a 21 pontos e a diferença de pontos entre os jogadores for maior ou
#    igual a dois;
# b) o jogador com mais de 21 pontos conseguir uma diferença de dois pontos sobre o adversário,
#    caso a primeira condição não seja atendida.
pontos_direita = 0
pontos_esquerda = 0

while True:
    ponto = input('Digite o código do ponto (D/E): ').strip().upper()

    if ponto == 'D':
        pontos_direita += 1
    elif ponto == 'E':
        pontos_esquerda += 1
    else:
        print('Código inválido!')
        continue

    diferenca = abs(pontos_direita - pontos_esquerda)

    if (pontos_direita >= 21 or pontos_esquerda >= 21) and diferenca >= 2:
        break

if pontos_direita > pontos_esquerda:
    print(f'Jogador da direita venceu por {pontos_direita} a {pontos_esquerda}!')
else:
    print(f'Jogador da esquerda venceu por {pontos_esquerda} a {pontos_direita}!')
