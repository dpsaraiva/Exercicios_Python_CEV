#Desafio: Crie um programa que vai ler vários números e coloque em uma lista.
# Depois disso crie duas listas extras que vão conter apenas os valores pares e os ímpares digitados, respectivamente.
# No final, mostre o conteúdo das três listas geradas.

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
