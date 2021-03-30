def aumentar(n=0, p=0, f=False):
    res = n * ((p/100) + 1)
    if f == True:
        return moeda(res)
    else:
        return res


def diminuir(n=0, p=0, f=False):
    res = n * (1 - (p/100))
    if f == True:
        return moeda(res)
    else:
        return res


def dobro(n=0, f=False):
    res = n * 2
    if f == True:
        return moeda(res)
    else:
        return res


def metade(n, f=False):
    res = n / 2
    if f == True:
        return moeda(res)
    else:
        return res


def moeda(n=0, moeda ='R$ '):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n, a, r):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado":<20}{moeda(n)}')
    print(f'{"Dobro do preço":<20}{dobro(n, True)}')
    print(f'{"Metade do preço":<20}{metade(n, True)}')
    print(f'{a}% {"de aumento":<16}{aumentar(n, a, True)}')
    print(f'{r}% {"de redução":<16}{diminuir(n, r, True)}')