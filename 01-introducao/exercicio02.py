# Exercício 2: Faça um algoritmo que leia uma temperatura em graus Fahrenheit e converta e mostre em
# graus Centígrados. FÓRMULA: Centigrados = (Fahrenheit - 32) * 5 / 9

graus_fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))

graus_centigrados = (graus_fahrenheit - 32) * 5 / 9

print(f'A temperatura em graus centígrados é {graus_centigrados:.2f}')