#Desafio: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele.

a = input('Digite algo: ')
print('Seu tipo primitivo é: ', type(a))
print('O conteúdo digitado é alfanumérico? ', a.isalnum())
print('O conteúdo digitado é alfabético? ', a.isalpha())
print('O conteúdo digitado é um dígito? ', a.isdigit())
print('O conteúdo digitado é um número? ', a.isnumeric())
print('O conteúdo digitado é um espaço? ', a.isspace())
print('O conteúdo digitado esta capitalizada? ', a.istitle())

