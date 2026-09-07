# Exercício 21: Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos
# 2 maiores.

valor_1 = float(input('Digite o primeiro valor: '))
valor_2 = float(input('Digite o segundo valor: '))
valor_3 = float(input('Digite o terceiro valor: '))

print('-' * 15)
if valor_1 > valor_3 and valor_2 > valor_3:
    print(f'A soma de {valor_1} + {valor_2} = {valor_1 + valor_2}')
elif valor_1 > valor_2 and valor_3 > valor_2:
    print(f'A soma de {valor_1} + {valor_3} = {valor_1 + valor_3}')
else:
    print(f'A soma de {valor_2} + {valor_3} = {valor_2 + valor_3}')