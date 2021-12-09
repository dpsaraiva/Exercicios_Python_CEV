#Desafio:Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

nome = input('Diga seu nome: ')
nome = nome.upper()
res = 'SILVA'in nome
print('Você tem Silva no nome?',res)
