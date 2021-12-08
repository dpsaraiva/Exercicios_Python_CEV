#Desafio: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
#mostre quantos dólares ela pode comprar. Considere $1,00 = R$3,27

n = float(input('Quanto dinheiro você tem na carteira? '))
print('Você pode comprar {}{:.2f} dólares'.format('\033[1;31m', n/3.27))
