# Exercício 6: Criar um algoritmo para ler a base e a altura de um triângulo e mostrar a sua área
# ((base x altura) / 2).

base = float(input('Informe qual é a base do triângulo: '))
altura = float(input('Informe qual é a altura do triângulo: '))

area = (base * altura) / 2

print(f'A área do triângulo é de {area:.2f}')