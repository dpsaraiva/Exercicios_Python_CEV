sal = float(input('Qual o seu salário? '))
if sal > 1250:
    aum = sal * 0.1
else:
    aum = sal * 0.15
print('O aumento será de R$ {:.2f}'.format(aum))
