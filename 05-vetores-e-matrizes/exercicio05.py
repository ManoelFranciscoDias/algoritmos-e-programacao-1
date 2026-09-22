# Exercício 5: Ler um vetor de 100 elementos numéricos e verificar se existem elementos iguais a
# 30. Se existirem, escrever as posições em que estão armazenados.

vetor = []
posicoes = []

for i in range(100):
    numero = int(input(f'Digite o {i+1}º elemento: '))
    vetor.append(numero)

    if numero == 30:
        posicoes.append(i)

if len(posicoes) >= 1:
    print('Existem elementos igual a 30 nesse vetor')
    print(f'posições: {posicoes}')
else:
    print('Não tem elementos iguais a 30 nesse vetor')