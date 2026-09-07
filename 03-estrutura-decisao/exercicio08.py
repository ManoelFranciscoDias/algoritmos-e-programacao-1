# Exercício 8: Entrar com a idade de uma pessoa e exibir a mensagem: Maior de idade, menor de idade ou
# acima de 65 anos.

idade = int(input('Digite a sua idade: '))

if idade < 0:
    print('Inválido!')
elif idade <= 17:
    print('Menor de idade')
elif idade <= 65:
    print('Maior de idade')
else:
    print('Acima de 65 anos')