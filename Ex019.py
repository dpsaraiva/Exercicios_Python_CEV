import random
a = input('Nome do 1º aluno: ')
b = input('Nome do 2º aluno: ')
c = input('Nome do 3º aluno: ')
d = input('Nome do 4º aluno: ')
lista = [a, b, c, d]
escolhido = random.choice(lista)
print('O aluno sorteado foi', escolhido)
