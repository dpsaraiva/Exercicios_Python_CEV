#Desafio: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista la dentro, ele não será adicionado.
# No final, serão exibidos todos os valores digitados, em ordem crescente.

cadastro = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in cadastro:
        print('Valor duplicado! Não vou adicionar...')
    else:
        cadastro.append(valor)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
cadastro.sort()
print(f'Você digitou os valores {cadastro}')
