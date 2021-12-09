#Desafio: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
#Seu programa tem que realizar três contagens através da função criada:
#a) De 1 até 10, de 1 em 1;
#b) De 10 até 0, de 2 em 2;
#c) Uma contagem personalizada.

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
