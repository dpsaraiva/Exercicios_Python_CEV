#Desafio: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

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


def leiaFloat(num):
    while True:
        try:
            num = str(input('Digite um número real: ')).strip().replace(',', '.')
            num = float(num)
        except (ValueError, TypeError):
            print(f'\033[31mERRO: \'{num}\' é um numero real inválido!\033[m')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número')
            return 0
        else:
            return num


#Programa Principal
n = leiaInt('Digite um número inteiro: ')
m = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {m}')
