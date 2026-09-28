# Exercício 20: Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior
# deles.

valor_1 = float(input('Digite o primeiro valor: '))
valor_2 = float(input('Digite o segundo valor: '))
valor_3 = float(input('Digite o terceiro valor: '))

if valor_1 > valor_2 and valor_1 > valor_3:
    print(f'O maior valor é {valor_1}')
elif valor_2 > valor_1 and valor_2 > valor_3:
    print(f'O maior valor é {valor_2}')
else:
    print(f'O maior valor é {valor_3}')
