# Exercício 12 (Valida e corrige número de telefone): Faça um programa que leia um número de
# telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na
# frente. O usuário pode informar o número com ou sem o traço separador.
#
# Exemplo:
# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

print('Valida e corrige número de telefone')

telefone = input('Telefone: ').strip()
numeros = telefone.replace('-', '')

if not numeros.isdecimal() or telefone.count('-') > 1:
    print('Telefone inválido. Digite somente os dígitos, com ou sem o traço separador.')
elif len(numeros) == 7:
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    numeros = '3' + numeros
    print(f'Telefone corrigido sem formatação: {numeros}')
    print(f'Telefone corrigido com formatação: {numeros[:4]}-{numeros[4:]}')
elif len(numeros) == 8:
    print('Telefone possui 8 dígitos. Não precisa de correção.')
    print(f'Telefone sem formatação: {numeros}')
    print(f'Telefone com formatação: {numeros[:4]}-{numeros[4:]}')
else:
    print('Telefone inválido. O número deve ter 7 ou 8 dígitos.')
