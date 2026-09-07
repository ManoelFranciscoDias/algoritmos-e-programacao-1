# Exercício 17: Refaça o algoritmo acima otimizando-o usando uma técnica conhecida por Pesquisa
# Binária. Suponha primeiramente que o vetor já esteja ordenado. Procuramos então o elemento K
# dividindo o vetor em duas partes e testando em qual das duas partes ele deveria estar.
# Procede-se então, da mesma forma para a parte provável, e assim sucessivamente.
# Obs.: na pesquisa sequencial simples (problema 16), o número médio de comparações que devem ser
# feitas até encontrar a chave é N/2, onde N é o número de elementos do vetor. No nosso caso, no
# algoritmo 16, teríamos, em média, 128/2 = 64 comparações. Na pesquisa binária, o número máximo
# de comparações é log2(N). Teríamos, então, log2(128) = 7 comparações, no máximo.
