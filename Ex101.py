#Desafio: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    atual = date.today().year
    ano = atual - ano
    if ano < 16:
        return 'Você não vota ainda.'
    elif 16 <= ano < 18 or ano > 65:
        return 'Voto facultativo.'
    else:
        return 'Voto OBRIGATÓRIO!'



ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
