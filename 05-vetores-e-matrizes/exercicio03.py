# Exercício 3: Repita o algoritmo acima, porém imprima quantos valores estão acima da média.

nota = []

for i in range(10):
    valor_nota = float(input(f'Digite a nota {i + 1}: '))

    while valor_nota < 0 or valor_nota > 10:
        print('Digite uma nota de 0 a 10')
        valor_nota = float(input(f'Digite a nota {i + 1}: '))

    nota.append(valor_nota)

media = sum(nota) / len(nota)

quantidade_acima_media = 0
for valor_nota in nota:
    if valor_nota > media:
        quantidade_acima_media += 1

print(f'A média das notas é {media:.2f}')
print(f'Quantidade de notas acima da média: {quantidade_acima_media}')
