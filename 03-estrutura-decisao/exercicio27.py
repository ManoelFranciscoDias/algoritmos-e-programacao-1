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