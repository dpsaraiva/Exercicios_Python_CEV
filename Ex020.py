#Desafio:O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
a = input('Nome do 1º aluno: ')
b = input('Nome do 2º aluno: ')
c = input('Nome do 3º aluno: ')
d = input('Nome do 4º aluno: ')
mylist = [a, b, c, d]
random.shuffle(mylist)
print('A ordem de apresentação é ', mylist)
