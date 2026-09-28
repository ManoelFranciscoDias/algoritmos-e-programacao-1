# Exercício 11: O governador acaba de liberar R$ 1.000.000.000,00 para construção de casas populares.
# Cada casa custa o equivalente a 90 salários mínimos. Faça um algoritmo que leia o valor
# do salário mínimo e calcule a quantidade de casas que podem ser construídas com o
# recurso liberado.

VERBA_LIBERADA = 1_000_000_000

salario_minimo = float(input('Informe o valor do salário mínimo: '))

valor_casa = salario_minimo * 90
quantidade_casas = int(VERBA_LIBERADA // valor_casa)

print(f'Com R$ 1.000.000.000,00 liberados pelo governo, é possível construir {quantidade_casas} casas')
