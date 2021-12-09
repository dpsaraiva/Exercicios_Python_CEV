#Desafio: Crie um programa que leia um número real e mostre a sua porção inteira.

n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {:.0f}'.format(n, n))

print('='*100)

from math import trunc
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, trunc(n)))

print('='*100)

n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, int(n)))
