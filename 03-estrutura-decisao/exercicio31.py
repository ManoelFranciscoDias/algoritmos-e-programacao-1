entrada = input('Digite um valor de 0 a 4: ')

if entrada.isdigit():
    opcao = int(entrada)

    if 0 <= opcao <= 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        if opcao == 0:
            resultado = num1 + num2
            print(f'A soma dos números é: {resultado}')
        elif opcao == 1:
            resultado = num1 - num2
            print(f'A subtração dos números é: {resultado}')
        elif opcao == 2:
            resultado = num1 * num2
            print(f'A multiplicação dos números é: {resultado}')
        elif opcao == 3:
            if num2 != 0:
                resultado = num1 / num2
                print(f'A divisão dos números é: {resultado}')
            else:
                print('Erro! Não é possível dividir por zero.')
        elif opcao == 4:
            resultado = (num1 + num2) / 2
            print(f'A média dos números é: {resultado}')
    else:
        print('Valor errado. Programa encerrado sem cálculos')
else:
    print('Valor errado. Programa encerrado sem cálculos')