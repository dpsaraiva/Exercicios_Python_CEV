#Desafio: Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
print('A sua média é {}{:.2f}'.format('\033[1;33m', (n1+n2)/2))
