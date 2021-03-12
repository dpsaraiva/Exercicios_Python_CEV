d = int(input('Dias de locação do veículo: '))
k = int(input('Quantos km rodados? '))
p = float(d * 60 + 0.15 * k)
print('O total a pagar é de R${:.2f}'.format(p))
