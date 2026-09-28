# Exercício 6: Escreva uma função que recebe 2 números inteiros n1 e n2 como
# entrada e retorna a soma de todos os números inteiros contidos no intervalo
# [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a
# soma.

def soma_intervalo(n1, n2):
    soma = 0
    for i in range(n1, n2 + 1):
        soma += i
    return soma


n1 = int(input('Informe o início do intervalo: '))
n2 = int(input('Informe o fim do intervalo: '))

resultado = soma_intervalo(n1, n2)
print(f'A soma dos números inteiros no intervalo [{n1}, {n2}] é {resultado}')
