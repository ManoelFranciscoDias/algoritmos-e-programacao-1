# Exercício 19: Ler 2 valores (considere que não serão lidos valores iguais) e escrevê-los em ordem
# crescente.

valor_1 = float(input('Digite o primeiro valor: '))
valor_2 = float(input('Digite o segundo valor: '))

if valor_1 > valor_2:
    print(f'{valor_2}, {valor_1}')
else:
    print(f'{valor_1}, {valor_2}')
