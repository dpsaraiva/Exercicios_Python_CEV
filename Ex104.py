#Desafio: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do python,
#só que fazendo a validação para aceitar apenas um valor numérico. Ex.: n = leiaInt("Digite um número:  ")

def leiaInt(num):
    while True:
        num = input('Digite um número: ').strip()
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
    return num


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
