print('=' * 20, '\033[1;31mCálculo Financiamento Bancário\033[m', '=' * 20)
valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
prazo = int(input('Em quantos anos pretende financiar? ')) * 12
res = float(valor / prazo)
if res <= salario * 0.3:
    print('Seu financiamento foi aprovado e o valor será R$ {:.2f} mensal'.format(res))
else:
    print('O valor da prestação excedeu 30% do salário. Seu financiamento foi \033[1;31mNEGADO')
