# Exercício 26: Faça um algoritmo que leia 3 valores a, b, c, e verifique se podem ser os comprimentos
# dos lados de um triângulo. Em caso afirmativo, verifique se é "triângulo equilátero",
# "triângulo isósceles" ou "triângulo escaleno". Em caso negativo, escreva a mensagem: "os
# valores lidos não formam um triângulo". Considere que o comprimento de cada lado é menor
# que a soma dos outros dois; um triângulo equilátero tem três lados iguais; um isósceles
# tem dois lados iguais e um diferente; um escaleno tem três lados diferentes.

a = float(input('Informe o primeiro lado do triângulo: '))
b = float(input('Informe o segundo lado do triângulo: '))
c = float(input('Informe o terceiro lado do triângulo: '))

if c < a + b and a < c + b and b < a + c:
    if a == b == c:
        print('Triângulo equilátero')
    elif a == b != c or a == c != b or b == c != a:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')
else:
    print('Os valores lidos não formam um triângulo')

