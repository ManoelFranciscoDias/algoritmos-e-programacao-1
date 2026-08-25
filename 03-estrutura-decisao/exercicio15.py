valor_produto = float(input('Informe o valor do produto: '))

if valor_produto < 20:
    print(f'O valor da venda é de R${(valor_produto * 1.45):.2f}')
else:
    print(f'O valor da venda é de R${(valor_produto * 1.30):.2f}')