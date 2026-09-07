# Exercício 17: Faça um algoritmo que verifique se uma letra digitada é vogal ou consoante.

letra = input('Informe uma letra: ').upper()

if letra.isalpha() and len(letra) == 1:
    if letra in 'AEIOU':
        print(f'A letra {letra} é uma vogal')
    else:
        print(f'A letra {letra} é uma consoante')
else:
    print('Digite uma letra')