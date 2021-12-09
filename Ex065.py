#Desafio: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
cont = 0
tot = 0
maior = 0
menor = 0
while continuar == 'S':
    num = int(input('Digite um número inteiro: '))
    continuar = input('Digite [S] para inserir outro número ou [N] para sair: ').upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        print('Opção INVÁLIDA')
        continuar = input('Digite [S] para inserir outro número ou [N] para sair: ').upper().strip()[0]
    cont += 1
    tot += num
    media = tot / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A média foi de {:.2f}'.format(media))
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))
