# Exercício 1: Faça uma função para converter uma temperatura em graus Fahrenheit
# para Celsius. A temperatura em Fahrenheit é o dado de entrada e a temperatura em
# Celsius é o dado de saída. Utilize a fórmula C = (F - 32) * 5/9, onde F é a
# temperatura em Fahrenheit e C é a temperatura em Celsius.

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperatura_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)

print(f'{temperatura_fahrenheit}°F equivalem a {temperatura_celsius:.2f}°C')
