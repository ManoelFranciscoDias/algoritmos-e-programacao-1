# Exercício 4: Entrar com um número e informar se ele é divisível por 5.

numero = float(input('Informe um número inteiro: '))

if numero % 5 == 0:
    print(f'{numero} é divisível por 5')
else:
    print(f'{numero} não é divisível por 5')