#Desafio: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

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
