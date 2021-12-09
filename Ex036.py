#Desafio: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ele não pode exceder 30% do salario do comprador,
#ou então o empréstimo será negado.

print('=' * 20, '\033[1;31mCálculo Financiamento Bancário\033[m', '=' * 20)
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
prazo = int(input('Em quantos anos pretende financiar? ')) * 12
res = float(valor / prazo)
if res <= salario * 0.3:
    print('Seu financiamento foi aprovado e o valor será R$ {:.2f} mensal'.format(res))
else:
    print('O valor da prestação excedeu 30% do seu salário. Seu financiamento foi \033[1;31mNEGADO')
