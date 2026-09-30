# Exercício 6 (Data por extenso): Faça um programa que solicite a data de nascimento
# (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
#
# Exemplo:
# Data de Nascimento: 29/10/1973
# Você nasceu em 29 de Outubro de 1973.

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

dia, mes, ano = input("Data de Nascimento: ").split("/")

print(f"Você nasceu em {dia} de {meses[int(mes) - 1]} de {ano}.")