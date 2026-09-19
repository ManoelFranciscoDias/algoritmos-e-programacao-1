# Exercício 15: Classificar um vetor numérico VET de 20 elementos em ordem crescente.

VET = []

for i in range(20):
    VET.append(float(input(f'Digite o {i+1}º número: ')))

VET.sort()
print(f'Números em ordem crescente: {VET}')