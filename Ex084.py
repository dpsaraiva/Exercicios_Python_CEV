cadastro = []
pesados = []
leves = []
continua = 's'
cont = maior = menor = 0
while continua in 'Ss':
    cadastro.append(str(input('Nome: ')))
    cadastro.append(int(input('Peso: ')))
    if cont == 0:
        maior = cadastro[1]
        menor = maior
    continua = input('Cadastrar mais? [S/N] ').upper().strip()[0]
    cont += 1
for i in range(0, len(cadastro), 2):
    if cadastro[i + 1] >= maior:
        if maior == cadastro[i + 1]:
            pesados.append(cadastro[i])
        else:
            maior = cadastro[i + 1]
            del(pesados)
            pesados = []
            pesados.append(cadastro[i])
    elif cadastro[i + 1] <= menor:
        if menor == cadastro[i + 1]:
            leves.append(cadastro[i])
        else:
            menor = cadastro[i + 1]
            del(leves)
            leves = []
            leves.append(cadastro[i])
print('=-' * 40)
print(f'Foram cadastradas {cont} pessoas')
print(f'O maior peso foi de {maior}. Peso de {pesados}')
print(f'O menor peso foi de {menor}. Peso de {leves}')
