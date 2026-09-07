# Exercício 27: Escreva um algoritmo que leia 4 valores (opção, a, b, c), onde opção é um valor inteiro
# e positivo e a, b, c são quaisquer valores reais. Se opção = 1, escreva os 3 valores em
# ordem crescente; se opção = 2, escreva os 3 valores em ordem decrescente; se opção = 3,
# escreva os valores de forma que o maior valor entre a, b, c fica entre os outros 2.

opcao = input('Informe a opção (1, 2 ou 3): ')

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

valores = [a, b, c]

if opcao == '1':
    valores.sort()
    print('Ordem crescente')
    print(valores)

elif opcao == '2':
    valores.sort(reverse=True)
    print('Ordem decrescente')
    print(valores)

elif opcao == '3':
    valores.sort()
    valores = [valores[0], valores[2], valores[1]]
    print('Maior no meio')
    print(valores)

else:
    print('Opção inválida')