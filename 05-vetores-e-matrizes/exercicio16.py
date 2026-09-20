# Exercício 16: Dado um vetor de 128 elementos, verificar se existe um elemento igual a K (chave)
# no vetor. Se existir, imprimir a posição onde foi encontrada a chave; se não, imprimir a
# mensagem: "CHAVE K NÃO ENCONTRADA". O vetor A e a chave K são lidos a partir de uma unidade de
# entrada.

K = int(input('Digite a chave K: '))

A = []
posicoes = []


for i in range(128):
    elemento = int(input(f'Digite o elemento {i+1}: '))
    A.append(elemento)

    if elemento == K:
        posicoes.append(i + 1)

if len(posicoes) == 0:
    print("CHAVE K NÃO ENCONTRADA")
else:
    print(f'Chave {K} encontrada na(s) posição(ões): {posicoes}')