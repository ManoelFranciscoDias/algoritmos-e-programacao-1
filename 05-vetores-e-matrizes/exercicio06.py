# Exercício 6: Fazer um algoritmo que calcule e escreva o somatório dos valores armazenados numa
# variável composta unidimensional (vetor) A, de 100 elementos numéricos a serem lidos do
# dispositivo de entrada.

A = []

for i in range(100):
    valores = float(input(f'Digite o {i+1}° elemento: '))
    A.append(valores)

print(f'O somatório dos valores armazenados é {sum(A)}')
