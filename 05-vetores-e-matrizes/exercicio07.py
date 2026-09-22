# Exercício 7: Escreva um algoritmo que leia um vetor de 200 valores numéricos reais e os imprima
# na ordem contrária em que foi lida.

vetor = []

for i in range(200):
    valor = float(input(f'Digite o {i+1}º valor: '))
    vetor.append(valor)

vetor.reverse()
print('O vetor na ordem contrária em que foi lido é:')
print(vetor)