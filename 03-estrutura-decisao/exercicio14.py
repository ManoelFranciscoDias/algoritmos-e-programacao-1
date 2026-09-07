# Exercício 14: Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens: "Carioca,
# Paulista, Mineiro ou Outros"

sigla = input('Informe a sigla do seu estado: ').upper()

if sigla == 'RJ':
    print('Carioca')
elif sigla == 'MG':
    print('Mineiro')
elif sigla == 'SP':
    print('Paulista')
else:
    print('Outros')