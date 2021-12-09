#Desafio: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Ate 14 anos: INFANTIL
# Ate 19 anos: JÚNIOR
# Ate 20 anos : SÊNIOR
# ACIMA: MASTER

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
