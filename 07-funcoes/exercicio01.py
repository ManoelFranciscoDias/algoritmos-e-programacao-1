# Exercício 1: Faça uma função para converter uma temperatura em graus Fahrenheit
# para Celsius. A temperatura em Fahrenheit é o dado de entrada e a temperatura em
# Celsius é o dado de saída. Utilize a fórmula C = (F - 32) * 5/9, onde F é a
# temperatura em Fahrenheit e C é a temperatura em Celsius.

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temp_f = float(input("Digite a temperatura em Fahrenheit: "))
temp_c = fahrenheit_para_celsius(temp_f)

print(f"{temp_f}°F equivalem a {temp_c:.2f}°C")