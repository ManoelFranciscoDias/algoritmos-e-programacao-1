# Exercício 18: Ler 2 valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valor_1 = float(input('Digite o primeiro valor: '))
valor_2 = float(input('Digite o segundo valor: '))

if valor_1 > valor_2:
    print(f'O maior valor é {valor_1}')
else:
    print(f'O maior valor é {valor_2}')