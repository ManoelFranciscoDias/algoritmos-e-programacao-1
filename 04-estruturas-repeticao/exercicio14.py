# Exercício 14: O valor aproximado do número π pode ser calculado usando-se a série:
# S = 1 - 1/3³ + 1/5³ - 1/7³ + 1/9³ - ...
# sendo o valor de π = raiz_cúbica(S x 32). Faça um algoritmo que calcule e escreva o valor de π
# usando os 51 primeiros termos da série.
S = 0
for i in range(51):
    denominador = (2 * i + 1) ** 3
    sinal = (-1) ** i
    S += sinal / denominador

pi = (S * 32) ** (1 / 3)
print("pi =", pi)
