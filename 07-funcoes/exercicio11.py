# Exercício 11: Crie uma função que realize a conversão de Polegadas (pol) para
# Centímetros (cm), onde pol é passado como parâmetro e cm é retornado.
# Sabe-se que 1 polegada tem 2.54 centímetros. Crie também um programa para
# testar tal função.

def polegadas_para_cm(pol):
    return pol * 2.54

polegadas = float(input('Informe o valor em polegadas: '))

cm = polegadas_para_cm(polegadas)

print(f'{polegadas} pol equivalem a {cm:.2f} cm')

