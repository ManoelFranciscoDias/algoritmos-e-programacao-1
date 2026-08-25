sigla = input('Informe a sigla do seu estado: ').upper()

if sigla == 'RJ':
    print('Carioca')
elif sigla == 'MG':
    print('Mineiro')
elif sigla == 'SP':
    print('Paulista')
else:
    print('Outros')