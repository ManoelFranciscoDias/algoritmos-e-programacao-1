# Exercício 22: Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem
# crescente.

valor_1 = float(input('Digite o primeiro valor: '))
valor_2 = float(input('Digite o segundo valor: '))
valor_3 = float(input('Digite o terceiro valor: '))

if valor_1 > valor_2 and valor_1 > valor_3 and valor_2 > valor_3:
    print(valor_3, valor_2, valor_1, sep=' - ')
elif valor_1 > valor_2 and valor_1 > valor_3 and valor_3 > valor_2:
    print(valor_2, valor_3, valor_1, sep=' - ')
elif valor_2 > valor_1 and valor_2 > valor_3 and valor_1 > valor_3:
    print(valor_3, valor_1, valor_2, sep=' - ')
elif valor_2 > valor_1 and valor_2 > valor_3 and valor_3 > valor_1:
    print(valor_1, valor_3, valor_2, sep=' - ')
elif valor_3 > valor_1 and valor_3 > valor_2 and valor_1 > valor_2:
    print(valor_2, valor_1, valor_3, sep=' - ')
else:
    print(valor_1, valor_2, valor_3, sep=' - ')
