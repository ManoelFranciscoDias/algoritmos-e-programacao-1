# Exercício 8: Escreva um algoritmo para fazer a soma de dois vetores de 10 elementos reais lidos
# do teclado. O primeiro elemento do primeiro vetor deverá ser adicionado ao primeiro elemento do
# segundo vetor e, o resultado deverá ser acumulado em um terceiro vetor também de 10 elementos.
# Imprimir os três vetores conforme layout de impressão abaixo:
# VETOR 1: __ __ __ __ __ __ __ __ __ __
# VETOR 2: __ __ __ __ __ __ __ __ __ __
# VETOR 3: __ __ __ __ __ __ __ __ __ __

vetor1 = []
vetor2 = []
vetor3 = []

print('Digite os 10 elementos do Vetor 1')
for i in range(10):
    valor = float(input(f'Digite o valor {i+1}: '))
    vetor1.append(valor)

print('Digite os 10 elementos do Vetor 2')
for i in range(10):
    valor = float(input(f'Digite o valor {i+1}: '))
    vetor2.append(valor)

for i in range(10):
    vetor3.append(vetor1[i] + vetor2[i])

print(f'Vetor 1 é: {vetor1}')
print(f'Vetor 2 é: {vetor2}')
print(f'A soma dos dois vetores é:')
print(vetor3)