#Desafio: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
# No final, mostre quantos numeros foram digitados e qual foi a soma entre eles. 

cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
if cont == 0:
    print('Nenhum número foi digitado')
elif cont == 1:
    print(f'Você digitou o número {soma}')
else:
    print(f'Você digitou {cont} números com soma igual a {soma}')
