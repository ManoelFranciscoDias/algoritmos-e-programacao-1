# Exercício 20: Uma máquina de biscoito está com problemas. Quando ligada, após 1 hora ela quebra
# 1 biscoito, na segunda hora ela quebra 3 biscoitos, na hora seguinte ela quebra 3 vezes a
# quantidade de biscoitos quebrados na hora anterior, e assim por diante. Faça um algoritmo que
# calcule quantos biscoitos são quebrados no final de cada dia (a máquina opera 16 horas por dia).

quebrados_hora = 1
total_dia = 0
horas_por_dia = 16

for hora in range(1, horas_por_dia + 1):
    total_dia += quebrados_hora
    print(f"Hora {hora}: {quebrados_hora} biscoito(s) quebrado(s) | Total acumulado: {total_dia}")
    quebrados_hora = quebrados_hora * 3

print("Total de biscoitos quebrados ao final do dia:", total_dia)