# Exercício 3: Dado um conjunto de valores inteiros positivos, determinar qual o menor e qual o
# maior valor do conjunto. Um número com valor "0" (zero) indica o fim dos dados e não deve ser
# considerado.
numero = int(input('Digite um número (0 para encerrar): '))

if numero == 0:
    print('Nenhum número foi digitado.')
else:
    maior = numero
    menor = numero

    while numero != 0:
        numero = int(input('Digite um número (0 para encerrar): '))
        
        if numero != 0:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero

    print(f'O maior valor digitado foi: {maior}')
    print(f'O menor valor digitado foi: {menor}')
