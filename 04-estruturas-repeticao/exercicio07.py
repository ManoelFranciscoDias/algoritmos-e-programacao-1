# Exercício 7: Faça um algoritmo que leia a quantidade de tinta que uma caneta tem, e enquanto a
# caneta tiver tinta para escrever, escreva "Enquanto tem tinta a caneta escreve...". Considere
# que a cada comando de escrita a caneta gasta 2% da tinta que possui.

quantidade_tinta = float(input('Qual a quantidade de tinta que a caneta tem? '))

while quantidade_tinta > 0.01:
    print('Enquanto tem tinta a caneta escreve...')
    quantidade_tinta = quantidade_tinta * 0.98


print('A caneta ficou sem tinta')

