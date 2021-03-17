total = cont = menor = item = 0
nome = ''
while True:
    produto = str(input('Nome do produto: '))
    item += 1
    preco = float(input('Preço: R$ '))
    if item == 1 or menor > preco:
        menor = preco
        nome = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
    total += (preco)
    if (preco) > 1000:
        cont += 1
print('Você gastou R${:.2f}, sendo {} com valor acima de R$ 1000,00'.format(total, cont))
print('O produto mais barato foi {} custando R$ {:.2f}'.format(nome, menor))
print('{:-^60}'.format('FIM DO PROGRAMA'))
