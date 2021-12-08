#Desafio: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

n = float(input('Digite o preço do produto: '))
print('Com 5% de desconto seu preço será R$ {:.2f}'.format(n*0.95))
