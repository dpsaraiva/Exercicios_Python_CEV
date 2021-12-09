#Desafio: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais um aumento de 15%.

sal = float(input('Qual o seu salário? '))
if sal > 1250:
    aum = sal * 0.1
else:
    aum = sal * 0.15
print('O aumento será de R$ {:.2f}'.format(aum))
