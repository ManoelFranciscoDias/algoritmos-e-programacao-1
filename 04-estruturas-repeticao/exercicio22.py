# Exercício 22: Faça um algoritmo que:
# - leia, para n pessoas, a altura e o sexo (sexo = 'M' ou sexo = 'm' para masculino e
#   sexo = 'F' ou sexo = 'f' para feminino);
# - escreva a média da altura das mulheres;
# - escreva a média da altura da turma.

n = int(input('Quantas pessoas deseja inserir a altura e sexo? '))

soma_alturas_femininas = 0
qtd_mulheres = 0
soma_alturas_totais = 0
qtd_pessoas_validas = 0

for i in range(1, n + 1):
    sexo = input(f'Digite o sexo da {i}° pessoa (M para masculino || F para feminino): ').upper()
    altura = float(input(f'Digite a altura da {i}° pessoa: '))

    if len(sexo) != 1:
        print('Digite apenas 1 caractere (M ou F).')
    else:
        if sexo == "F":
            qtd_mulheres += 1
            soma_alturas_femininas += altura
            soma_alturas_totais += altura
            qtd_pessoas_validas += 1
        elif sexo == "M":
            soma_alturas_totais += altura
            qtd_pessoas_validas += 1
        else:
            print('Digite apenas 1 caractere (M ou F).')

if qtd_mulheres > 0:
    media_altura_mulheres = soma_alturas_femininas / qtd_mulheres
    print(f'A média da altura das mulheres é {media_altura_mulheres:.2f}')
else:
    print('Nenhuma mulher foi cadastrada.')

if qtd_pessoas_validas > 0:
    media_altura_turma = soma_alturas_totais / qtd_pessoas_validas
    print(f'A média da altura da turma é {media_altura_turma:.2f}')
else:
    print('Nenhuma pessoa foi cadastrada corretamente.')