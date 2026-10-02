# Exercício 1: Fazer um algoritmo para ler o valor do lado de um quadrado e mostrar sua área
# (lado^2) e seu perímetro (4 x lado).

lado_quadrado = float(input('Informe a medida do lado do quadrado: '))

area = lado_quadrado**2
perimetro = 4 * lado_quadrado

print(f'A área do quadrado é {area:.2f} e o seu perímetro é {perimetro:.2f}')
