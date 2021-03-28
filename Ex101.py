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