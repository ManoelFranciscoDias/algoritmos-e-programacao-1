# Exercício 6 (Data por extenso): Faça um programa que solicite a data de nascimento
# (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
#
# Exemplo:
# Data de Nascimento: 29/10/1973
# Você nasceu em 29 de Outubro de 1973.

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

partes = input("Data de Nascimento: ").split("/")

if len(partes) != 3 or not partes[1].isdecimal() or not 1 <= int(partes[1]) <= 12:
    print("Data inválida. Use o formato dd/mm/aaaa.")
else:
    dia, mes, ano = partes
    print(f"Você nasceu em {dia} de {meses[int(mes) - 1]} de {ano}.")