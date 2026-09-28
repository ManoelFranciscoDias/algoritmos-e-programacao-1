# Exercício 13: Escreva um algoritmo que:
# a) leia uma frase de 50 caracteres;
# b) conte quantos brancos existem na frase;
# c) conte quantas vezes a letra "A" aparece;
# d) imprima o que foi calculado nos itens b e c

frase = input('Digite uma frase de 50 caracteres: ')

while len(frase) != 50:
    print(f'A frase tem {len(frase)} caracteres. Tente novamente.')
    frase = input('Digite uma frase de 50 caracteres: ')

quantidade_espacos = 0
quantidade_letra_a = 0

for caractere in frase:
    if caractere == ' ':
        quantidade_espacos += 1
    elif caractere.upper() == 'A':
        quantidade_letra_a += 1

print(f'Frase: {frase}')
print(f'Espaços em branco: {quantidade_espacos}')
print(f'Quantidade de letras A: {quantidade_letra_a}')
