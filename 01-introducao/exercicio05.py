# Exercício 5: Faça um algoritmo que leia as 3 notas de um aluno e calcule e escreva a média final
# deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5,
# respectivamente.

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))

media = ((nota_1 * 2) + (nota_2 * 3) + (nota_3 * 5)) / 10

print(f'A média final é {media:.2f}')