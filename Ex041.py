from datetime import date
ano_atual = date.today().year
ano = int(input('Informe seu ano de nascimento com 4 digitos: '))
idade = ano_atual - ano
if idade <= 9:
    print('Categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Categoria Infantil')
elif idade > 14 and idade <= 17:
    print('Categoria Júnior')
elif idade > 17 and idade <= 20:
    print('Categoria Sênior')
else:
    print('Categoria Master')
