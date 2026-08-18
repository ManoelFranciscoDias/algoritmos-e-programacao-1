salario_bruto = float(input('Informe qual é o seu salario bruto mensal: '))

ir = salario_bruto * 0.15
inss = salario_bruto * 0.11
sindicato = salario_bruto * 0.03
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f'Salario Bruto_______R${salario_bruto:.2f}')
print(f'IR__________________R${ir:.2f}')
print(f'INSS________________R${inss:.2f}')
print(f'Sindicato___________R${sindicato:.2f}')
print(f'Salario Liquido_____R${salario_liquido:.2f}')