# Exercício 25: Um hotel cobra R$ 50,00 de diária por hóspede e mais uma taxa de serviços. A taxa
# de serviços é de:
# - R$ 7,50 por diária, caso o número de diárias seja menor que 15;
# - R$ 6,50 por diária, caso o número de diárias seja igual a 15;
# - R$ 5,00 por diária, caso o número de diárias seja maior que 15.
# Faça um algoritmo que apresente as seguintes opções ao recepcionista:
# 1. encerrar a conta de um hóspede
# 2. verificar número de contas encerradas
# 3. finalizar a execução
# Caso a opção escolhida seja a primeira, leia o nome e o número de diárias do hóspede e escreva
# o nome e total a ser pago. Caso a opção escolhida seja a segunda, informe o número de hóspedes
# que deixaram o hotel (número de contas encerradas).
contas_encerradas = 0

while True:
    print('\n1. Encerrar a conta de um hóspede')
    print('2. Verificar número de contas encerradas')
    print('3. Finalizar a execução')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        nome_hospede = input('Digite o nome do hóspede: ')
        num_diarias = int(input('Digite o número de diárias: '))

        if num_diarias < 15:
            taxa_servico = 7.50
        elif num_diarias == 15:
            taxa_servico = 6.50
        else:
            taxa_servico = 5.00

        total_pagar = num_diarias * (50.00 + taxa_servico)
        contas_encerradas += 1
        print(f'{nome_hospede}, o total a pagar é de R${total_pagar:.2f}')
    elif opcao == 2:
        print(f'Número de contas encerradas: {contas_encerradas}')
    elif opcao == 3:
        print('Encerrando o sistema...')
        break
    else:
        print('Opção inválida!')
