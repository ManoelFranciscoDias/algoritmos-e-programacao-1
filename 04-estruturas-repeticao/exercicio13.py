# Exercício 13: Fazer um algoritmo para calcular o valor de S, dado por:
# S = 1/N + 2/(N-1) + 3/(N-2) + ... + (N-1)/2 + N/1, sendo N lido.
N = int(input("Digite N: "))
S = 0
for i in range(1, N + 1):
    S += i / (N - i + 1)
print("S =", S)
