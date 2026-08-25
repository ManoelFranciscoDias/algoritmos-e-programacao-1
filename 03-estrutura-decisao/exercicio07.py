from datetime import datetime

ano_atual = datetime.now().year

ano_nascimento = int(input("Digite o ano de nascimento: "))

if ano_nascimento > 0 and ano_nascimento <= ano_atual:
    idade = ano_atual - ano_nascimento
    print(f"Idade: {idade} anos")
else:
    print("Ano inválido!")
    