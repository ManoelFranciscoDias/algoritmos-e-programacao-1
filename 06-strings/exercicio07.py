# Exercício 7 (Conta espaços e vogais): Dado uma string com uma frase informada pelo usuário
# (incluindo espaços em branco), conte:
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Digite uma frase: ").lower()

print("Espaços em branco:", frase.count(" "))

for vogal in "aeiou":
    print(f'Vogal {vogal}: {frase.count(vogal)}')

