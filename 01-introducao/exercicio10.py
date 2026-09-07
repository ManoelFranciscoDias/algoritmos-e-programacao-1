# Exercício 10: Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em
# segundos e mostre-o expresso em horas, minutos e segundos.

duracao_segundos = int(input('Quanto tempo o evento durou em segundos: '))

horas = duracao_segundos // 3600
minutos = (duracao_segundos % 3600) // 60
segundos = duracao_segundos % 60

print(f'Isso equivale a {horas} horas, {minutos} minutos e {segundos} segundos')