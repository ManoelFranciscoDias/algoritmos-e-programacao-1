# Exercício 33: Escreva um algoritmo que leia as idades de 2 homens e 2 mulheres (considere que as
# idades dos homens serão sempre diferentes, bem como as das mulheres). Calcule e escreva
# a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do
# homem mais novo com a mulher mais velha.

idade_homem_1 = int(input('Digite a idade do primeiro homem: '))
idade_homem_2 = int(input('Digite a idade do segundo homem: '))
idade_mulher_1 = int(input('Digite a idade da primeira mulher: '))
idade_mulher_2 = int(input('Digite a idade da segunda mulher: '))

if idade_homem_1 > idade_homem_2 and idade_mulher_1 > idade_mulher_2:
    print(f'A soma do homem mais velho com a mulher mais nova é {idade_homem_1 + idade_mulher_2}')
    print(f'O produto do homem mais novo com a mulher mais velha é {idade_homem_2 * idade_mulher_1}')

if idade_homem_1 > idade_homem_2 and idade_mulher_2 > idade_mulher_1:
    print(f'A soma do homem mais velho com a mulher mais nova é {idade_homem_1 + idade_mulher_1}')
    print(f'O produto do homem mais novo com a mulher mais velha é {idade_homem_2 * idade_mulher_2}')

if idade_homem_2 > idade_homem_1 and idade_mulher_1 > idade_mulher_2:
    print(f'A soma do homem mais velho com a mulher mais nova é {idade_homem_2 + idade_mulher_2}')
    print(f'O produto do homem mais novo com a mulher mais velha é {idade_homem_1 * idade_mulher_1}')

if idade_homem_2 > idade_homem_1 and idade_mulher_2 > idade_mulher_1:
    print(f'A soma do homem mais velho com a mulher mais nova é {idade_homem_2 + idade_mulher_1}')
    print(f'O produto do homem mais novo com a mulher mais velha é {idade_homem_1 * idade_mulher_2}')