# Exercício 5 (Nome na vertical em escada invertida): Altere o programa anterior de modo que a
# escada seja invertida.
#
# Exemplo (nome = FULANO):
# FULANO
# FULAN
# FULA
# FUL
# FU
# F

nome = input('Digite o seu nome: ').upper()

for i in range(len(nome), 0, -1):
    print(nome[:i])