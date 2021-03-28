def contador(inicio, fim, passo):
    from time import sleep
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('FIM!')


#Programa Princpal
contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 30)
print('Agora é a sua vez de personalizar')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)