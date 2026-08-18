salario_bruto = float(input('Informe qual é o seu salario bruto mensal: '))

ir = salario_bruto * 0.15
inss = salario_bruto * 0.11
sindicato = salario_bruto * 0.03
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f'{"Salario Bruto":<20}R${salario_bruto:.2f}')
print(f'{"(-) IR (15%)":<20}R${ir:.2f}')
print(f'{"(-) INSS (11%)":<20}R${inss:.2f}')
print(f'{"(-) Sindicato (3%)":<20}R${sindicato:.2f}')
print(f'{"Salario Liquido":<20}R${salario_liquido:.2f}')