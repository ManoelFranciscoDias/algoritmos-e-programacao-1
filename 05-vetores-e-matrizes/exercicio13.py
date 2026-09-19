# Exercício 13: Escreva um algoritmo que:
# a) leia uma frase de 50 caracteres;
# b) conte quantos brancos existem na frase;
# c) conte quantas vezes a letra "A" aparece;
# d) imprima o que foi calculado nos itens b e c.

# Exercício 13

frase = input('Digite uma frase de 50 caracteres: ')

while len(frase) != 50:
    print(f'A frase tem {len(frase)} caracteres. Tente novamente.')
    frase = input('Digite uma frase de 50 caracteres: ')

espacos_brancos = 0
letra_a = 0

for caractere in frase:
    if caractere == " ":
        espacos_brancos += 1
    elif caractere.upper() == "A":
        letra_a += 1

print(f'Na frase: {frase}')
print(f'Possui {letra_a} letras A')
print(f'E {espacos_brancos} espaços em branco')