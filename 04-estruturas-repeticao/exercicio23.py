# Exercício 23: Uma loja de departamentos oferece para seus clientes um determinado desconto de
# acordo com o valor da compra efetuada. O desconto é de 20% caso o valor da compra seja maior
# que R$ 500,00 e de 15% caso seja menor ou igual. Faça um algoritmo que leia, para cada cliente,
# nome, endereço e valor da compra e escreva o total a pagar. Um nome de cliente igual a ULTIMO
# indica o fim da entrada de dados.

while True:
    nome_cliente = input('Digite o nome do cliente (use ULTIMO para encerrar): ').upper()

    if nome_cliente == "ULTIMO":
        print('FIM!')
        break

    endereco_cliente = input('Digite o seu endereço: ')
    valor_compra = float(input('Digite o valor da compra: '))

    if valor_compra > 500:
        total_a_pagar = valor_compra * 0.80
    else:
        total_a_pagar = valor_compra * 0.85

    print(f'{nome_cliente}, o total a pagar é de R${total_a_pagar:.2f}')