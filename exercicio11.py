salario_minimo = float(input('Informe qual é o preço do salario minimo: '))

valor_casa = salario_minimo * 90
quantidade_casas = 1_000_000_000 // valor_casa

print(f'Com R$1.000.000.000,00 liberado do governo, podemos criar {quantidade_casas:.0f} casas')