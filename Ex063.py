num = int(input('Digite um número: '))
termos = int(input('Quantos termos você quer? '))
res = 0
cont = 1
aux = 0
while cont <= termos:
    res = res + aux
    aux = num
    num = res
    print(res, end=' - ')
    cont += 1
print('FIM')
