#Desafio: Crie um algoritmo que leia um número e mostre o seu dobro.

n = int(input('Digite um número inteiro: '))
print('Seu dobro é {}{}\033[m, seu triplo é {}{}\033[m e sua raiz quadrada é {:.2f}'.format('\033[1;34m', n*2, '\033[1;36m', n*3, n**(1/2)))
