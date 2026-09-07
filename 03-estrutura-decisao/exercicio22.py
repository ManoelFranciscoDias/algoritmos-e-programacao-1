# Exercício 22: Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem
# crescente.

nmr1 = float(input('Digite o primeiro valor: '))
nmr2 = float(input('Digite o segundo valor: '))
nmr3 = float(input('Digite o terceiro valor: '))

if nmr1 > nmr2 and nmr1 > nmr3 and nmr2 > nmr3:
    print(nmr3, nmr2, nmr1, sep=' - ')
elif nmr1 > nmr2 and nmr1 > nmr3 and nmr3 > nmr2:
    print(nmr2, nmr3, nmr1, sep=' - ')
elif nmr2 > nmr1 and nmr2 > nmr3 and nmr1 > nmr3:
    print(nmr3, nmr1, nmr2, sep=' - ')
elif nmr2 > nmr1 and nmr2 > nmr3 and nmr3 > nmr1:
    print(nmr1, nmr3, nmr2, sep=' - ')
elif nmr3 > nmr1 and nmr3 > nmr2 and nmr1 > nmr2:
    print(nmr2, nmr1, nmr3, sep=' - ')
else:
    print(nmr1, nmr2, nmr3, sep=' - ')