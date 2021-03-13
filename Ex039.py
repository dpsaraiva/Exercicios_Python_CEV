from datetime import date
ano = int(input('Informe seu ano de nascimento com 4 digitos: ')) + 18
ano_atual = date.today().year
if ano == ano_atual:
    print('É o ano do seu alistamento militar!')
elif ano > ano_atual:
    print('Falta {} anos para seu alistamento militar.'.format(ano - ano_atual))
else:
    print('Você passou {} anos do seu alistamento militar!'.format(ano_atual - ano))
