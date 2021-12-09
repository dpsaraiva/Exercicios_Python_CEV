#Desafio: Faça um programa que leia um número qualquer e mostre seu fatorial.
# Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

num = int(input('Digite um número inteiro: '))
num1 = num
res = num
while res > 1:
    num = num * (res - 1)
    res = res - 1
print('O fatorial de {} é {}'.format(num1, num))
