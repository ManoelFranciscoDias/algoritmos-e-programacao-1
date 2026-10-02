# Exercício 13 (Jogo da palavra embaralhada): Desenvolva um jogo em que o usuário tenha que
# adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista
# de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis
# tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando
# se o usuário ganhou ou perdeu o jogo.

import os
import random

caminho = os.path.join(os.path.dirname(__file__), 'palavras.txt')

with open(caminho, encoding='utf-8') as arquivo:
    palavras = [linha.strip().upper() for linha in arquivo if linha.strip()]

palavra = random.choice(palavras)

embaralhada = palavra
while embaralhada == palavra:
    embaralhada = ''.join(random.sample(palavra, len(palavra)))

print('Jogo da palavra embaralhada')
print(f'Palavra embaralhada: {embaralhada}')
print()

tentativas = 6
ganhou = False

while tentativas > 0 and not ganhou:
    palpite = input('Qual é a palavra? ').strip().upper()

    if palpite == palavra:
        ganhou = True
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f'-> Você errou. Restam {tentativas} tentativa(s).')
        print()

if ganhou:
    print(f'Parabéns, você ganhou! A palavra era {palavra}.')
else:
    print(f'Você perdeu! A palavra era {palavra}.')
