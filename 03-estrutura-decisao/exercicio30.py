# Exercício 30: Faça um algoritmo para controle de temperatura de um forno que derrete alumínio. O
# programa deverá perguntar a temperatura de trabalho e operar assim: temperatura <= 500°C
# = "Temperatura Inválida"; < 700°C = "Aquecimento Ligado em 100%"; < 735°C = "Aquecimento
# Ligado em 50%"; >= 735°C = "Aquecimento Desligado"; > 780°C = "Superaquecimento". Os
# valores digitados devem ser inteiros e inferiores a 1000.

temperatura = int(input('Qual a temperatura que o alumínio deverá ser trabalhado: '))

if temperatura >= 1000:
    print('Erro! Digite valores inferiores a 1000')
elif temperatura <= 500:
    print('Temperatura Inválida')
elif temperatura < 700:
    print('Aquecimento Ligado em 100%')
elif temperatura < 735:
    print('Aquecimento Ligado em 50%')
elif temperatura <= 780:
    print('Aquecimento Desligado')
else:
    print('Superaquecimento')