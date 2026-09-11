# Exercício 4: Faça um algoritmo que calcule e escreva a soma dos números pares e a soma dos
# números ímpares entre 1 e 100.

contador = 1
soma_par = 0
soma_impar = 0

while contador <= 100:
    if contador % 2 == 0:
        soma_par += contador
    else:
        soma_impar += contador
    contador += 1

print(f'A soma dos números pares é {soma_par}')
print(f'A soma dos números impares é {soma_impar}')

