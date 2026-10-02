# Exercício 27: Um motorista acaba de voltar de um feriado prolongado. Antes de sair de viagem e
# imediatamente após retornar, o motorista encheu o tanque do veículo e registrou as medidas do
# odômetro. Em cada parada feita durante a viagem, foi registrado o valor do odômetro e a
# quantidade de combustível comprado para reabastecer o veículo (suponha que o tanque ficou vazio
# e foi enchido a cada parada). Faça um algoritmo que leia o número total de reabastecimentos
# feitos (incluindo o primeiro) e os dados registrados relativos à compra de combustível. Calcule
# e escreva:
# a) a quilometragem obtida por litro de combustível entre cada par de paradas
# b) a quilometragem média obtida por litro de combustível em toda a viagem.

pergunta = 'Digite o número total de reabastecimentos (incluindo o primeiro): '
quantidade_reabastecimentos = int(input(pergunta))

pergunta = 'Digite a leitura do odômetro no primeiro abastecimento, antes de sair: '
odometro_anterior = float(input(pergunta))
odometro_inicial = odometro_anterior

litros_total = 0

# O primeiro abastecimento já foi lido acima; os demais são as paradas e o retorno
for parada in range(1, quantidade_reabastecimentos):
    odometro_atual = float(input(f'Digite a leitura do odômetro no {parada + 1}º abastecimento: '))
    litros = float(input('Digite a quantidade de combustível comprada (em litros): '))

    while litros <= 0:
        print('Quantidade inválida! Digite um valor maior que zero.')
        litros = float(input('Digite a quantidade de combustível comprada (em litros): '))

    distancia = odometro_atual - odometro_anterior
    km_por_litro = distancia / litros
    print(f'Quilometragem obtida nesse trecho: {km_por_litro:.2f} km/L')

    litros_total += litros
    odometro_anterior = odometro_atual

if litros_total > 0:
    distancia_total = odometro_anterior - odometro_inicial
    media_geral = distancia_total / litros_total
    print(f'Quilometragem média da viagem: {media_geral:.2f} km/L')
else:
    print('São necessários pelo menos 2 abastecimentos para calcular a média.')
