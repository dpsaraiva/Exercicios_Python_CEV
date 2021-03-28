def sorteia(num):
    from random import randint
    from time import sleep
    print('Sorteando os 5 valores da lista: ',end='')
    for i in range(0, 5):
        num.append(randint(1, 10))
        print(num[i], end=' ')
        sleep(0.5)
    print('PRONTO')


def somapar(num):
    par = 0
    for i in num:
        if i % 2 == 0:
            par += i
    print(f'Somando os valores{num}, temos: {par}')

nums = []
sorteia(nums)
somapar(nums)
