# Exercício 5: Escreva um programa para ler o número de lados de um polígono
# regular e a medida do lado (em cm). Faça uma função que receba como parâmetro
# o número de lados e a medida do lado deste polígono e calcule e imprima o
# seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu
#   perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5.

def classificar_poligono(qtd_lados, lado):
    if qtd_lados == 3:
        print(f'TRIÂNGULO | Perímetro: {lado * 3:.2f} cm')
    elif qtd_lados == 4:
        print(f'QUADRADO | Área: {lado ** 2:.2f} cm²')
    elif qtd_lados == 5:
        print('PENTÁGONO')


qtd_lados = int(input('Informe o número de lados do polígono: '))
lado = float(input('Informe a medida do lado (cm): '))

classificar_poligono(qtd_lados, lado)