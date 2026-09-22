# Exercício 32: Uma matriz X[n][4] contém informações sobre alunos de uma universidade. Os
# índices das linhas são os números de matrícula e os elementos da 1a, 2a, 3a e 4a colunas são,
# respectivamente, idade, sexo (0 ou 1), curso (no. do curso) e nota. Fazer um algoritmo para
# obter o aluno do sexo 0, curso 6, que obteve a melhor nota. Supor a inexistência de empate.

n = int(input('Digite o número de alunos: '))

X = []
for i in range(n):
    print(f'Digite os dados do aluno de matrícula {i}')
    idade = int(input('Idade: '))
    sexo = int(input('Sexo (0 ou 1): '))
    curso = int(input('Curso: '))
    nota = float(input('Nota: '))
    X.append([idade, sexo, curso, nota])

matricula_melhor = -1
melhor_nota = -1

for i in range(n):
    sexo = X[i][1]
    curso = X[i][2]
    nota = X[i][3]

    if sexo == 0 and curso == 6 and nota > melhor_nota:
        matricula_melhor = i
        melhor_nota = nota

if matricula_melhor == -1:
    print('Nenhum aluno do sexo 0 e curso 6 encontrado')
else:
    print(f'Aluno com a melhor nota: matrícula {matricula_melhor}, nota {melhor_nota}')
