# Exercício 11 (Jogo de Forca): Desenvolva um jogo da forca. O programa terá uma lista de
# palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6
# vezes antes de ser enforcado.
#
# Exemplo:
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
#
# Digite uma letra: O
# A palavra é: _ _ _ _ O
#
# Digite uma letra: E
# A palavra é: _ E _ _ O
#
# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

import os
import random

caminho = os.path.join(os.path.dirname(__file__), "palavras.txt")

with open(caminho, encoding="utf-8") as arquivo:
    palavras = [linha.strip().upper() for linha in arquivo if linha.strip()]

palavra = random.choice(palavras)
descobertas = ["_"] * len(palavra)
tentadas = []
erros = 0

print("Jogo da Forca")
print("A palavra é:", " ".join(descobertas))
print()

while erros < 6 and "_" in descobertas:
    letra = input("Digite uma letra: ").strip().upper()

    if len(letra) != 1 or not letra.isalpha():
        print("-> Digite apenas uma letra.")
    elif letra in tentadas:
        print(f"-> Você já tentou a letra {letra}.")
    else:
        tentadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    descobertas[i] = letra
            print("A palavra é:", " ".join(descobertas))
        else:
            erros += 1
            if erros < 6:
                print(f"-> Você errou pela {erros}ª vez. Tente de novo!")
            else:
                print(f"-> Você errou pela {erros}ª vez.")

    print()

if "_" not in descobertas:
    print(f"Parabéns! Você acertou a palavra {palavra}.")
else:
    print(f"Você foi enforcado! A palavra era {palavra}.")
