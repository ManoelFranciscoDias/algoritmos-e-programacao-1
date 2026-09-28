# Exercício 15: Classificar um vetor numérico VET de 20 elementos em ordem crescente

VET = []

for i in range(20):
    VET.append(float(input(f'Digite o {i + 1}º número: ')))

# Bubble sort: a cada passada, o maior elemento restante "sobe" para o final do vetor
for i in range(len(VET) - 1):
    for j in range(len(VET) - 1 - i):
        if VET[j] > VET[j + 1]:
            VET[j], VET[j + 1] = VET[j + 1], VET[j]

print(f'Números em ordem crescente: {VET}')
