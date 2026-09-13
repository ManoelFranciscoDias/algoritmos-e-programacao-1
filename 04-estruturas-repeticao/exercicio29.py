# Exercício 29: Os regulamentos de uma competição de pesca impõem um limite no peso total de
# pesca de um dia. Faça um algoritmo que leia o limite diário (em quilogramas) e então leia o
# peso (em gramas) de cada peixe e escreva o peso total da pesca obtido até aquele ponto. Quando
# o limite diário for excedido escreva uma mensagem e encerre a execução do algoritmo. O
# algoritmo deve ainda apresentar ao usuário a seguinte mensagem: "informar o peso de mais um
# peixe: s (SIM) / n (NÃO)?" antes de prosseguir com a entrada de dados.
limite_diario_kg = float(input('Digite o limite diário de pesca (em Kg): '))
limite_diario_g = limite_diario_kg * 1000

peso_total = 0

while True:
    peso_peixe = float(input('Digite o peso do peixe (em gramas): '))
    peso_total += peso_peixe

    print(f'Peso total da pesca até o momento: {peso_total} gramas')

    if peso_total > limite_diario_g:
        print('Limite diário excedido! Encerrando a execução.')
        break

    continuar = input('Informar o peso de mais um peixe: s (SIM) / n (NÃO)? ').strip().upper()
    if continuar == 'N':
        break
