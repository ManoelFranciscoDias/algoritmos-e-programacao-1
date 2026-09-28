# Exercício 33: Escreva um algoritmo que leia as idades de 2 homens e 2 mulheres (considere que as
# idades dos homens serão sempre diferentes, bem como as das mulheres). Calcule e escreva
# a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do
# homem mais novo com a mulher mais velha.

idade_homem_1 = int(input('Digite a idade do primeiro homem: '))
idade_homem_2 = int(input('Digite a idade do segundo homem: '))
idade_mulher_1 = int(input('Digite a idade da primeira mulher: '))
idade_mulher_2 = int(input('Digite a idade da segunda mulher: '))

if idade_homem_1 > idade_homem_2:
    homem_mais_velho = idade_homem_1
    homem_mais_novo = idade_homem_2
else:
    homem_mais_velho = idade_homem_2
    homem_mais_novo = idade_homem_1

if idade_mulher_1 > idade_mulher_2:
    mulher_mais_velha = idade_mulher_1
    mulher_mais_nova = idade_mulher_2
else:
    mulher_mais_velha = idade_mulher_2
    mulher_mais_nova = idade_mulher_1

soma = homem_mais_velho + mulher_mais_nova
produto = homem_mais_novo * mulher_mais_velha

print(f'A soma das idades do homem mais velho com a mulher mais nova é {soma}')
print(f'O produto das idades do homem mais novo com a mulher mais velha é {produto}')
