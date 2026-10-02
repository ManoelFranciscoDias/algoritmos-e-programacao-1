# Exercício 14 (Leet spek generator): Leet é uma forma de se escrever o alfabeto latino usando
# outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite
# muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo
# dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se
# como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça
# um programa que peça uma texto e transforme-o para a grafia leet speak.

leet = {"a": "4", "b": "8", "e": "3", "g": "6", "i": "1",
        "o": "0", "s": "5", "t": "7", "z": "2"}

texto = input("Digite um texto: ")

texto_leet = ""
for caractere in texto:
    texto_leet += leet.get(caractere.lower(), caractere)

print(f"Texto em leet speak: {texto_leet}")
