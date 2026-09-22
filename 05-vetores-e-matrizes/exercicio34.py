# Exercício 34: Sabe-se que a multiplicação de duas matrizes A e B só é possível se o número de
# colunas da matriz A for igual ao número de linhas da matriz B. Assim, se A é uma matriz m x n e
# B uma matriz n x p, a multiplicação será possível e o produto será uma matriz C(m x p). O
# produto matricial pode ser muito útil em várias aplicações como, por exemplo, na situação
# descrita a seguir.
#
# Uma certa fábrica produziu dois tipos de motores M1 e M2 nos meses de janeiro a dezembro e o
# número de motores produzidos foi registrado na tabela a seguir:
#         M1    M2
# JAN     30    20
# FEV     5     10
# MAR     7     15
# ...
# DEZ     18    25
#
# O setor de controle de vendas tem uma tabela do custo e do lucro (em milhares de reais) obtidos
# com cada motor.
#         CUSTO   LUCRO
# M1      10      3
# M2      15      2
#
# Para saber o custo e o lucro nos meses de janeiro a dezembro, basta que se faça o produto
# matricial das duas tabelas.
#
# Portanto, fazer um algoritmo que, a partir da produção mensal de motores M1 e M2 e seus
# respectivos custos e lucros, calcule o custo e o lucro em cada um dos meses e o custo e lucro
# anuais.

MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

producao = []
print('Digite a produção mensal dos motores M1 e M2')
for i in range(12):
    m1 = int(input(f'{MESES[i]} - quantidade de M1: '))
    m2 = int(input(f'{MESES[i]} - quantidade de M2: '))
    producao.append([m1, m2])

custo_lucro = []
print('Digite o custo e o lucro de cada motor (em milhares de reais)')
for motor in ('M1', 'M2'):
    custo = float(input(f'Custo do motor {motor}: '))
    lucro = float(input(f'Lucro do motor {motor}: '))
    custo_lucro.append([custo, lucro])

resultado = []
for i in range(12):
    custo_mes = 0
    lucro_mes = 0
    for k in range(2):
        custo_mes += producao[i][k] * custo_lucro[k][0]
        lucro_mes += producao[i][k] * custo_lucro[k][1]
    resultado.append([custo_mes, lucro_mes])

custo_anual = 0
lucro_anual = 0

print('\nCusto e lucro mensais:')
for i in range(12):
    print(f'{MESES[i]}: custo = R$ {resultado[i][0]:.2f} | lucro = R$ {resultado[i][1]:.2f}')
    custo_anual += resultado[i][0]
    lucro_anual += resultado[i][1]

print(f'\nCusto anual: R$ {custo_anual:.2f}')
print(f'Lucro anual: R$ {lucro_anual:.2f}')
