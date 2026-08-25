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