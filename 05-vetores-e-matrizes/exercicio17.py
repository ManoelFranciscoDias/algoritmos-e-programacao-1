# Exercício 17: Refaça o algoritmo acima otimizando-o usando uma técnica conhecida por Pesquisa
# Binária. Suponha primeiramente que o vetor já esteja ordenado. Procuramos então o elemento K
# dividindo o vetor em duas partes e testando em qual das duas partes ele deveria estar.
# Procede-se então, da mesma forma para a parte provável, e assim sucessivamente.
# Obs.: na pesquisa sequencial simples (problema 16), o número médio de comparações que devem ser
# feitas até encontrar a chave é N/2, onde N é o número de elementos do vetor. No nosso caso, no
# algoritmo 16, teríamos, em média, 128/2 = 64 comparações. Na pesquisa binária, o número máximo
# de comparações é log2(N). Teríamos, então, log2(128) = 7 comparações, no máximo.

import random

N = 128

vetor = sorted(random.sample(range(1, 1001), N))

print("Vetor ordenado:")
print(vetor)

K = int(input("\nDigite o valor K a ser procurado: "))

inicio = 0
fim = N - 1
posicao = -1
comparacoes = 0

while inicio <= fim:
    meio = (inicio + fim) // 2
    comparacoes += 1

    if vetor[meio] == K:
        posicao = meio
        break
    elif K < vetor[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1

if posicao != -1:
    print(f"\nO valor {K} foi encontrado na posição {posicao} (índice do vetor).")
else:
    print(f"\nO valor {K} não está no vetor.")

print(f"Número de comparações realizadas: {comparacoes}")
