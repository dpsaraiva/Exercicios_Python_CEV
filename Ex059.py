oper = 0
while oper == 0:
    print('=-=' * 15)
    val1 = float(input('Digite o 1º valor: '))
    val2 = float(input('Digite o 2º valor: '))
    res = 0
    oper = int(input('O que você deseja fazer?\n'
                     '[1] somar\n'
                     '[2] multiplicar\n'
                     '[3] maior\n'
                     '[4] novos números\n'
                     '[5] sair do programa\n'))
    while oper not in range(1, 6):
        oper = int(input('Opção INVÁLIDA\n'
                         'O que você deseja fazer?\n'
                         '[1] somar\n'
                         '[2] multiplicar\n'
                         '[3] maior\n'
                         '[4] novos números\n'
                         '[5] sair do programa\n'))
    while oper in range(1, 5):
        if oper == 1:
            res = val1 + val2
            print('A soma entre {} e {} é {:.2f}.'.format(val1, val2, res))
            oper = 0
        elif oper == 2:
            res = val1 * val2
            print('A multiplicação entre {} e {} é {:.2f}'.format(val1, val2, res))
            oper = 0
        elif oper == 3:
            if val1 > val2:
                print('O maior valor entre {} e {} é {}'.format(val1, val2, val1))
                oper = 0
            elif val2 > val1:
                print('O maior valor entre {} e {} é {}'. format(val1, val2, val2))
                oper = 0
            else:
                print('Os dois valores são iguais')
                oper = 0
        elif oper == 4:
           oper = 0
        else:
            oper = 6
print('Fim do Programa')
