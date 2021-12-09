#Desafio: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
#O primeiro que indique o número a calcular e o outro chamado show, que será um valor
#logico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do fatorial de um número num.
    '''
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(i, end=' ')
            if i > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f


print(fatorial(9, True))
help(fatorial)
