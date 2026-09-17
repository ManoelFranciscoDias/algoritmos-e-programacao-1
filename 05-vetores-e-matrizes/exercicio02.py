# Exercício 2: Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável
# composta chamada NOTA e calcule e imprima a sua média.
nota = []
for i in range(10):
    n = float(input(f'Digite a nota {i+1}: '))

    while n < 0 or n > 10:
        print('Digite uma nota de 0 a 10')
        n = float(input(f'Digite a nota {i+1}: '))

    nota.append(n)

media = sum(nota) / len(nota)
print(f'A média das notas é {media:.2f}')