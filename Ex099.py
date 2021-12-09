#Desafio: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analizar todos os valores e dizer qual deles é maior.

def maior(* num):
    from time import sleep
    print('=-' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    ma = 0
    if len(num) == 1:
        print(num[0])
        sleep(0.5)
        print(f'Foi informado {len(num)} valor ao todo.')
        ma = num[0]
        print(f'O maior valor informado foi {ma}')
    elif len(num) > 1:
        for i in num:
            if ma < i:
                ma = i
            print(i, end=' ')
            sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {ma}')
    else:
        print('Você não digitou nenhum número')
    sleep(1)


#Programa Principal

maior(55, 22, 33, 2, 0, 458, 3, 1500, 8, 77)
maior(55)
maior()
