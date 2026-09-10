# Exercício 8: Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de
# inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva:
# - o número de inscrição e a altura do atleta mais alto;
# - o número de inscrição e a altura do atleta mais baixo;
# - a altura média do grupo de atletas.
quantidade_atletas = int(input('Digite quantos atletas deseja cadastrar: '))
soma_alturas = 0
posicao_atual = 1

while posicao_atual <= quantidade_atletas:
    inscricao_atleta = int(input(f'Digite o número de inscrição do {posicao_atual}° atleta: '))
    altura_atleta = float(input(f'Digite a altura (em cm) do {posicao_atual}° atleta: '))
    soma_alturas += altura_atleta

    if posicao_atual == 1:
        altura_mais_alto = altura_atleta
        inscricao_mais_alto = inscricao_atleta
        altura_mais_baixo = altura_atleta
        inscricao_mais_baixo = inscricao_atleta
    else:
        if altura_atleta > altura_mais_alto:
            altura_mais_alto = altura_atleta
            inscricao_mais_alto = inscricao_atleta
        if altura_atleta < altura_mais_baixo:
            altura_mais_baixo = altura_atleta
            inscricao_mais_baixo = inscricao_atleta

    posicao_atual += 1

media_alturas = soma_alturas / quantidade_atletas

print(f'O atleta mais alto tem inscrição {inscricao_mais_alto} e altura {altura_mais_alto} cm')
print(f'O atleta mais baixo tem inscrição {inscricao_mais_baixo} e altura {altura_mais_baixo} cm')
print(f'A altura média do grupo é de: {media_alturas:.2f} cm')