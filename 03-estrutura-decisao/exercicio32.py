# Exercício 32: Escrever um algoritmo que leia valores inteiros em duas variáveis distintas e, se o
# resto da divisão da primeira pela segunda for 1, mostre a soma das variáveis mais o
# resto da divisão; se for 2, escreva se o primeiro e o segundo valor são pares ou
# ímpares; se for igual a 3, multiplique a soma dos valores lidos pelo primeiro; se for
# igual a 4, divida a soma dos números lidos pelo segundo (se este for diferente de zero);
# em qualquer outra situação, mostre o quadrado dos números lidos.

numero_1 = int(input('Digite o primeiro número inteiro: '))
numero_2 = int(input('Digite o segundo número inteiro: '))

if numero_2 == 0:
    print('Não é possível dividir por zero: o segundo número deve ser diferente de 0')
else:
    resto = numero_1 % numero_2
    soma = numero_1 + numero_2

    if resto == 1:
        print(f'A soma dos números mais o resto da divisão é: {soma + resto}')
    elif resto == 2:
        if numero_1 % 2 == 0:
            print('O primeiro valor é par')
        else:
            print('O primeiro valor é ímpar')

        if numero_2 % 2 == 0:
            print('O segundo valor é par')
        else:
            print('O segundo valor é ímpar')
    elif resto == 3:
        print(f'A soma dos valores multiplicada pelo primeiro é: {soma * numero_1}')
    elif resto == 4:
        print(f'A soma dos valores dividida pelo segundo é: {soma / numero_2}')
    else:
        print(f'O quadrado do primeiro número é: {numero_1 ** 2}')
        print(f'O quadrado do segundo número é: {numero_2 ** 2}')
