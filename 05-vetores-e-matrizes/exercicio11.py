# Exercício 11: Faça um algoritmo que leia um conjunto de 10 elementos reais e os coloque em um
# vetor. Construa um segundo vetor formado da seguinte maneira:
# - Os elementos de ordem par são os correspondentes do primeiro vetor multiplicados por 3.
# - Os elementos de ordem ímpar são os correspondentes do primeiro vetor divididos por 2.
# - Imprima os dois vetores.

vetor_1 = []

for i in range(10):
    valor = float(input(f'Digite o {i+1}º valor numérico: '))
    vetor_1.append(valor)

vetor_2 = []

for i in range(10):
    ordem = i + 1
    if ordem % 2 == 0:
        vetor_2.append(vetor_1[i] * 3)
    else:
        vetor_2.append(vetor_1[i] / 2)

print('Vetor 1:', vetor_1)
print('Vetor 2:', vetor_2)
