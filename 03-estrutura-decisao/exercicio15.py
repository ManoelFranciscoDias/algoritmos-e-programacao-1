# Exercício 15: Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da
# compra for menor que R$ 20,00; Caso contrário, o lucro será de 30%. Entrar com o valor
# do produto e imprimir o valor da venda.

valor_produto = float(input('Informe o valor do produto: '))

if valor_produto < 20:
    print(f'O valor da venda é de R${(valor_produto * 1.45):.2f}')
else:
    print(f'O valor da venda é de R${(valor_produto * 1.30):.2f}')