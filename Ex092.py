#Desafio: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um discionário, 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

ficha = {}
from datetime import date
ficha['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento:'))
ficha['Idade'] = date.today().year - nasc
ficha['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['CTPS'] != 0:
    ficha['Ano contratacao'] = int(input('Ano de contratação: '))
    ficha['Salario'] = float(input('Salário R$: '))
    ficha['Aposentadoria'] = ficha['Idade'] + ((ficha['Ano contratacao'] + 35) - date.today().year)
print('-=' * 30)
for k, v in ficha.items():
    print(f'  - {k} tem valor {v}.')
