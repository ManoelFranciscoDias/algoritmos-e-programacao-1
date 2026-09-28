# Exercício 8: Escreva um algoritmo para fazer a soma de dois vetores de 10 elementos reais lidos
# do teclado. O primeiro elemento do primeiro vetor deverá ser adicionado ao primeiro elemento do
# segundo vetor e, o resultado deverá ser acumulado em um terceiro vetor também de 10 elementos.
# Imprimir os três vetores conforme layout de impressão abaixo:
# VETOR 1: __ __ __ __ __ __ __ __ __ __
# VETOR 2: __ __ __ __ __ __ __ __ __ __
# VETOR 3: __ __ __ __ __ __ __ __ __ __

vetor_1 = []
vetor_2 = []
vetor_3 = []

print('Digite os 10 elementos do Vetor 1')
for i in range(10):
    valor = float(input(f'Digite o valor {i+1}: '))
    vetor_1.append(valor)

print('Digite os 10 elementos do Vetor 2')
for i in range(10):
    valor = float(input(f'Digite o valor {i+1}: '))
    vetor_2.append(valor)

for i in range(10):
    vetor_3.append(vetor_1[i] + vetor_2[i])

print(f'VETOR 1: {" ".join(str(valor) for valor in vetor_1)}')
print(f'VETOR 2: {" ".join(str(valor) for valor in vetor_2)}')
print(f'VETOR 3: {" ".join(str(valor) for valor in vetor_3)}')
