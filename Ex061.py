prim_termo = int(input('Digite o 1º termo: '))
razao = int(input('Qual a razão dessa PA? '))
cont = 1
res = prim_termo
print('Os 10 primeiros termos dessa PA são: ', end='')
while cont <= 10:
    print('{} - '.format(res), end='')
    res = res + razao
    cont += 1
print('FIM')
