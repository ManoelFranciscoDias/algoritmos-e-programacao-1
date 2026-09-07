# Exercício 8: O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
# distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem
# do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo
# de fábrica de um carro e escreva o custo ao consumidor.

custo_fabrica = float(input('Digite qual foi o custo da fábrica: '))
porcentagem_distribuidor = 28
porcentagem_impostos = 45

soma_porcentagem = 1 + (porcentagem_distribuidor / 100) + (porcentagem_impostos / 100)
custo_consumidor = custo_fabrica * soma_porcentagem

print(f'O custo ao consumidor será de: R${custo_consumidor:.2f}')