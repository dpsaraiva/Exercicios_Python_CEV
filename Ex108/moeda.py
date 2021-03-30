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
