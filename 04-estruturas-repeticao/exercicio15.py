# Exercício 15: Fazer um algoritmo que calcule e escreva a soma dos 20 primeiros termos da série:
# 100/0! + 99/1! + 98/2! + 97/3! + ...
import math
soma = 0

for i in range(20):
    numerador = 100 - i
    denominador = math.factorial(i)
    termo = numerador / denominador
    soma += termo

print(f'A soma dos 20 primeiros termos é: {soma:.4f}')