# Exercício 32: Escrever um algoritmo que leia valores inteiros em duas variáveis distintas e, se o
# resto da divisão da primeira pela segunda for 1, mostre a soma das variáveis mais o
# resto da divisão; se for 2, escreva se o primeiro e o segundo valor são pares ou
# ímpares; se for igual a 3, multiplique a soma dos valores lidos pelo primeiro; se for
# igual a 4, divida a soma dos números lidos pelo segundo (se este for diferente de zero);
# em qualquer outra situação, mostre o quadrado dos números lidos.

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

resto = num1 % num2

if resto == 1:
    soma = num1 + num2
    print(f'A soma dos números mais o resto da divisão é: {soma + resto}')

elif resto == 2:
    if num1 % 2 == 0:
        print('O primeiro valor é par')
    else:
        print('O primeiro valor é ímpar')

    if num2 % 2 == 0:
        print('O segundo valor é par')
    else:
        print('O segundo valor é ímpar')

elif resto == 3:
    soma = num1 + num2
    resultado = soma * num1
    print(f'A soma dos valores multiplicada pelo primeiro é: {resultado}')

elif resto == 4:
    soma = num1 + num2
    if num2 != 0:
        resultado = soma / num2
        print(f'A soma dos números dividida pelo segundo é: {resultado}')
    else:
        print('Não é possível dividir por zero')

else:
    print(f'O quadrado do primeiro número é: {num1 ** 2}')
    print(f'O quadrado do segundo número é: {num2 ** 2}')