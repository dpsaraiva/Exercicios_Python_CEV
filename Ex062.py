prim_termo = int(input('Digite o 1º termo: '))
razao = int(input('Qual a razão dessa PA? '))
cont = 1
res = prim_termo
max = 10
print('Os 10 primeiros termos dessa PA são: ', end='')
while cont <= max:
    if cont == max:
        print(res)
        print('Quantos termos a mais você deseja saber? Ou digite "0" para encerrar')
        max += int(input())
        res = res + razao
    else:
        print('{} - '.format(res), end='')
        res = res + razao
    cont += 1
print('FIM')
