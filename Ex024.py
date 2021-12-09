#Desafio:Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome 'Santo'.

texto = input('Qual o nome da sua cidade? ')
texto = texto.lstrip()
texto = texto.capitalize()
res = 'Santo'in texto
print('O nome da cidade começa com Santo?', res)
