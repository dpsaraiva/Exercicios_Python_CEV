#Desafio: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite o valor em metros: '))
print('Em centímetros será {}{:.0f}\033[m cm\nEm milímetros será {}{:.0f}\033[m mm'.format('\033[1;41m', n*100, '\033[1;42m', n*1000))
