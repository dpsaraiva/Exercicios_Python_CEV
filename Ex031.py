dis = int(input('Qual a distância da viagem em km? '))
if dis <= 200:
    valor = float(dis * 0.5)
else:
    valor = float(dis * 0.45)
print('O valor da passagem é R$ {:.2f}'.format(valor))
