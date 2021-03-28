from time import sleep
c = ('\033[m',          # 0 - sem cor
     '\033[0;97;42m',   # 1 - fundo verde fonte branca
     '\033[0;97;104m',  # 2 - fundo azul fonte branca
     '\033[0;97;41m',   # 3 - fundo vermelho fonte branca
     '\033[30;107m'     # 4 - fundo branco fonte preta
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(c[0], end='')
    sleep(1)


#Progrma principal
palavra = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    palavra = str(input('Função ou Biblioteca > '))
    if palavra.upper() == 'FIM':
        break
    else:
        ajuda(palavra)
titulo('ATÉ LOGO', 3)
