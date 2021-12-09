#Desafio:Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Diga seu nome: ')
nome = nome.strip()
nome = nome.upper()
pri_nome = nome.split()
ult_nome = nome.rsplit(' ', 1)
print('Nome completo: {}'.format(nome))
print('Seu primeiro nome é: {}'.format(pri_nome[0]))
print('Seu último nome é: {}'.format(ult_nome[1]))
