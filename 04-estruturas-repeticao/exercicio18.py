# Exercício 18: Uma companhia de teatro planeja dar uma série de espetáculos. A direção calcula
# que, a R$ 5,00 o ingresso, serão vendidos 120 ingressos. Com a diminuição de R$ 0,50 no preço
# dos ingressos, espera-se que haja um aumento de 26 ingressos vendidos. As despesas estão
# estipuladas em R$ 200,00 independente do número de ingressos vendidos. Faça um algoritmo que
# escreva uma tabela contendo o preço do ingresso, o número de ingressos e o lucro esperado em
# função do preço do ingresso, fazendo-se variar este preço de R$ 5,00 a R$ 1,00 de R$ 0,50 em
# R$ 0,50. Escreva também o lucro máximo esperado, o preço e o número de ingressos
# correspondentes.

despesas = 200.00
lucro_maximo = None

print(f"{'Preço':>8} {'Ingressos':>10} {'Lucro':>10}")

for i in range(10, 1, -1):
    preco = i / 2
    reducoes = 10 - i
    ingressos = 120 + reducoes * 26
    lucro = preco * ingressos - despesas

    print(f"{preco:8.2f} {ingressos:10d} {lucro:10.2f}")

    if lucro_maximo is None or lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_otimo = preco
        ingressos_otimo = ingressos

print(f"\nLucro máximo: R$ {lucro_maximo:.2f}")
print(f"Preço do ingresso: R$ {preco_otimo:.2f}")
print(f"Número de ingressos: {ingressos_otimo}")