idade_dias = int(input('Informe a sua idade em dias: '))

anos = idade_dias // 365
resto_dias = idade_dias % 365

meses = resto_dias // 30
dias = resto_dias % 30

print(f'Você tem {anos} anos, {meses} meses e {dias} dias')
