#Desafio: Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
soma = n1 + n2
print('A soma entre {} e {} é igual a {}{}\033[m' .format(n1, n2, '\033[30;41m', soma))
