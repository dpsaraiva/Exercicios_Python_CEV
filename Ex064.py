num = 0
tot = 0
cont = -1
while num != 999:
    tot += num
    cont += 1
    num = int(input('Digite um número qualquer ou 999 para sair: '))
if cont == 0:
    print('Nenhum número foi digitado')
elif cont == 1:
    print('O número digitado foi {}'.format(tot))
else:
    print('Você digitou {} números com soma igual a {} '.format(cont, tot))
