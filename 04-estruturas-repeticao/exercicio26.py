# Exercício 26: Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
# Dada a sua massa inicial em Kg, faça um algoritmo que determine o tempo necessário para que essa
# massa se torne menor que 0,5 gramas. Escreva a massa inicial, a massa final e o tempo.
massa_inicial = float(input('Digite a massa inicial (em Kg): '))

massa_atual = massa_inicial * 1000
tempo = 0

while massa_atual >= 0.5:
    massa_atual /= 2
    tempo += 50

print(f'Massa inicial: {massa_inicial} Kg')
print(f'Massa final: {massa_atual:.4f} gramas')
print(f'Tempo necessário: {tempo} segundos')
