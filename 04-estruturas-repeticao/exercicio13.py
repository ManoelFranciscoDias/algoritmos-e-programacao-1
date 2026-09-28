# Exercício 13: Fazer um algoritmo para calcular o valor de S, dado por:
# S = 1/N + 2/(N-1) + 3/(N-2) + ... + (N-1)/2 + N/1, sendo N lido.

n = int(input('Digite o valor de N: '))
s = 0

for i in range(1, n + 1):
    s += i / (n - i + 1)

print(f'S = {s:.4f}')
