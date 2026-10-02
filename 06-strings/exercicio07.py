# Exercício 7 (Conta espaços e vogais): Dado uma string com uma frase informada pelo usuário
# (incluindo espaços em branco), conte:
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Digite uma frase: ").lower()

print("Espaços em branco:", frase.count(" "))

vogais = {"a": "aáàâã", "e": "eéê", "i": "ií", "o": "oóôõ", "u": "uúü"}

for vogal, variacoes in vogais.items():
    quantidade = 0
    for letra in variacoes:
        quantidade += frase.count(letra)
    print(f'Vogal {vogal}: {quantidade}')

