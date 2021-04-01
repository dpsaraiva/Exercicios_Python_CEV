def leiaInt(num):
    while True:
        try:
            num = int(input(num))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: \'{num}\' é um numero inteiro inválido!\033[m')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua Opção: \033[m')
    return opc


