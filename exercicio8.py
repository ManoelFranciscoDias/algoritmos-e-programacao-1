custo_fabrica = float(input('Digite qual foi o custo da fábrica: '))
porcentagem_distribuidor = 28
porcentagem_impostos = 45

soma_porcentagem = 1 + (porcentagem_distribuidor / 100) + (porcentagem_impostos / 100)
custo_consumidor = custo_fabrica * soma_porcentagem

print(f'O custo do consumidor será de: R${custo_consumidor:.2f}')