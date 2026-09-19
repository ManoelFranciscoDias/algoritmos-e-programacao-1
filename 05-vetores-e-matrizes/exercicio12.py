# Exercício 12: Escreva um algoritmo que:
# a) leia um conjunto A de 20 elementos a partir de uma unidade de entrada;
# b) calcule e imprima o valor de S, onde:
# S = (A[0] - A[19])² + (A[1] - A[18])² + ... + (A[9] - A[10])²

A = []
S = 0

for i in range(20):
    elemento = float(input(f'Digite o {i+1}º elemento: '))
    A.append(elemento)

for i in range(10):
    S += (A[i] - A[19 - i])**2

print('S =', S)
