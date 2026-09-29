# Exercício 1 (Tamanho de strings): Faça um programa que leia 2 strings e informe o conteúdo
# delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento
# e são iguais ou diferentes no conteúdo.
#
# Exemplo:
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

print("Compara duas strings")
s1 = input("String 1: ")
s2 = input("String 2: ")

print(f'Tamanho de "{s1}": {len(s1)} caracteres')
print(f'Tamanho de "{s2}": {len(s2)} caracteres')

if len(s1) == len(s2):
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")

if s1 == s2:
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")