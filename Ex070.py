continua = 'S'
total = cont = 0
while continua in 'Ss':
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    total += preco
    if preco > 1000:
        cont += 1
print('O total da compra foi R$ {:.2f}. Você comprou {} produtos acima de R$ 1000,00'.format(total, cont))
