import random
a = input('Nome do 1º aluno: ')
b = input('Nome do 2º aluno: ')
c = input('Nome do 3º aluno: ')
d = input('Nome do 4º aluno: ')
mylist = [a, b, c, d]
random.shuffle(mylist)
print('A ordem de apresentação é ', mylist)
