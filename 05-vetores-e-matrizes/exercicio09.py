# Exercício 9: Fazer um algoritmo que:
# a) Leia duas variáveis compostas unidimensionais, contendo, cada uma, 25 elementos numéricos;
# b) intercale os elementos desses dois conjuntos formando uma nova variável composta
#    unidimensional de 50 elementos;
# c) Escreva o resultado obtido.

vetor1 = []
vetor2 = []
vetor_intercalado = []

print('Digite os 25 valores do vetor 1: ')
for i in range(25):
    valor = float(input(f'Digite o {i+1}º valor: '))
    vetor1.append(valor)

print('Digite os 25 valores do vetor 2: ')
for i in range(25):
    valor = float(input(f'Digite o {i+1}º valor: '))
    vetor2.append(valor)

for i in range(25):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])

print('Intercalando os dois vetores temos:')
print(vetor_intercalado)