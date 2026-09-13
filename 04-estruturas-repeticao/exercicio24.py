# Exercício 24: Faça um algoritmo que leia valores, sendo que cada valor representa a idade de
# uma pessoa. Calcule e escreva a idade média do grupo de pessoas. Só devem ser computados no
# cálculo valores maiores do que zero. O algoritmo deve apresentar ao usuário a seguinte
# mensagem: "deseja digitar mais um valor: s (SIM) / n (NAO)?", antes de prosseguir com a entrada
# de dados.
total_pessoas = 0
soma_idades = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))

    if idade > 0:
        total_pessoas += 1
        soma_idades += idade
    else:
        print('Idade inválida — digite um valor maior que 0.')

    continuar = input('Deseja digitar mais um valor? s (SIM) / n (NAO): ').strip().upper()
    if continuar == 'N':
        break

if total_pessoas > 0:
    media = soma_idades / total_pessoas
    print(f'A idade média do grupo é {media:.1f} anos.')
else:
    print('Nenhuma idade válida foi digitada.')