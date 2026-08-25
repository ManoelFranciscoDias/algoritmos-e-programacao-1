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

