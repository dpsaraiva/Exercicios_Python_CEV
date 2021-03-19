num = list()
numpar = list()
numimpar = list()
while True:
    num.append(int(input('Digite um número: ')))
    continua = input('Quer continuar: [S/N]').upper().strip()[0]
    if continua == 'N':
        break
for v in num:
    if v % 2 == 0:
        numpar.append(v)
    else:
        numimpar.append(v)
print(f'A lista completa é {num}')
print(f'A lista de pares é {numpar}')
print(f'A lista de ímpares é {numimpar}')
