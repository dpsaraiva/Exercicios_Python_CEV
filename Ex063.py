#Desafio: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

num = int(input('Digite um número: '))
termos = int(input('Quantos termos você quer? '))
res = 0
cont = 1
aux = 0
while cont <= termos:
    res = res + aux
    aux = num
    num = res
    print(res, end=' - ')
    cont += 1
print('FIM')
