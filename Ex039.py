#Desafio: Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar;
#Se é a hora dele se alistar;
#Se ele ja passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Informe seu ano de nascimento com 4 digitos: ')) + 18
ano_atual = date.today().year
if ano == ano_atual:
    print('É o ano do seu alistamento militar!')
elif ano > ano_atual:
    print('Falta {} anos para seu alistamento militar.'.format(ano - ano_atual))
else:
    print('Você passou {} anos do seu alistamento militar!'.format(ano_atual - ano))
