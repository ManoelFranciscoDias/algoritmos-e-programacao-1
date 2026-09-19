# Exercício 10: Escreva um algoritmo que:
# a) leia 100 valores numéricos e os armazene numa variável composta unidimensional A;
# b) calcule e escreva: S = somatório de i / a[i], para i de 0 a 99, onde a[i] é o i-ésimo valor
#    armazenado na variável A;
# c) calcule e escreva quantos termos da série acima têm o numerador menor do que o denominador.

A = []

print('Digite 100 valores numéricos')
for i in range(100):
    valor = float(input(f'Digite o {i+1}° valor numérico: ').replace(',', '.'))
    A.append(valor)

S = 0
contador = 0

for i in range(100):
    if A[i] == 0:
        print(f'Termo {i} ignorado: A[{i}] é zero (divisão por zero).')
        continue

    S += i / A[i]

    if i < A[i]:
        contador += 1

print(f'S = {S:.4f}')
print(f'Termos com numerador menor que o denominador: {contador}')