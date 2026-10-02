# Exercício 4 (Nome na vertical em escada): Modifique o programa anterior de forma a mostrar o
# nome em formato de escada.
#
# Exemplo (nome = FULANO):
# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = input('Nome: ').upper()


for i in range(1, len(nome) + 1):
    print(nome[:i])
