# Exercício 6: Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa
# nasceu).

ano_atual = int(input('Informe o ano atual: '))
ano_nascimento = int(input('Informe o seu ano de nascimento: '))

idade = ano_atual - ano_nascimento

if idade >= 16:
    print('Você poderá votar este ano!')
else:
    print('Você ainda não poderá votar este ano!')
