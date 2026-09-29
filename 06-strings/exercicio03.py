# Exercício 3 (Nome na vertical): Faça um programa que solicite o nome do usuário e imprima-o na
# vertical.
#
# Exemplo (nome = FULANO):
# F
# U
# L
# A
# N
# O

print("Nome na vertical")

nome = input("Digite o seu nome: ").upper()

for letra in nome:
    print(letra)