duracao_segundos = int(input('Quanto tempo o evento durou em segundos: '))

horas = duracao_segundos // 3600
minutos = (duracao_segundos % 3600) // 60
segundos = duracao_segundos % 60

print(f'Isso equivale a {horas} horas, {minutos} minutos e {segundos} segundos')