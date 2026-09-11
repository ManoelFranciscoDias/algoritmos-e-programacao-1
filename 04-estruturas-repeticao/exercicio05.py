# Exercício 5: Faça um algoritmo que leia a altura de 20 pessoas e calcule a média aritmética
# das alturas.

contador = 1
soma_altura = 0

while contador <= 20:
    altura = float(input(f'Digite a altura da {contador}ª pessoa: '))

    if altura <= 0:
        print('Altura inválida! Digite um valor maior que zero.')
    else:
        soma_altura += altura
        contador += 1


print(f'A média aritmetica das alturas é {(soma_altura / 20):.2f}')
