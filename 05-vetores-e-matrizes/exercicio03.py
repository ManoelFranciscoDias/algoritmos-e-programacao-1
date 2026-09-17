# Exercício 3: Repita o algoritmo acima, porém imprima quantos valores estão acima da média.

nota = []

for i in range(10):
    n = float(input(f'Digite a nota {i+1}: '))

    while n < 0 or n > 10:
        print('Digite notas de 0 a 10')
        n = float(input(f'Digite a nota {i+1}: '))

    nota.append(n)

media = sum(nota) / len(nota)

acima_media = []
for n in nota:
    if n > media:
        acima_media.append(n)

print(f'A média das notas é {media:.2f}')
print('As notas acima da média são:')
print(acima_media)

