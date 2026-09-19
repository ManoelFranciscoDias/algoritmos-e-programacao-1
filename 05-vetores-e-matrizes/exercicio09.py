# Exercício 9: Fazer um algoritmo que:
# a) Leia duas variáveis compostas unidimensionais, contendo, cada uma, 25 elementos numéricos;
# b) intercale os elementos desses dois conjuntos formando uma nova variável composta
#    unidimensional de 50 elementos;
# c) Escreva o resultado obtido.

variavel_1 = []
variavel_2 = []
variavel_3 = []

print('Digite os 25 valores da variavel 1: ')
for i in range(25):
    valor = float(input(f'Digite o {i+1} valor: '))
    variavel_1.append(valor)

print('Digite os 25 valores da variavel 2: ')
for i in range(25):
    valor = float(input(f'Digite o {i+1} valor: '))
    variavel_2.append(valor)

for i in range(25):
    variavel_3.append(variavel_1[i])
    variavel_3.append(variavel_2[i])

print('Intercalando as duas variaveis temos:')
print(variavel_3)