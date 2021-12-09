#Desafio: Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$ 0,50/km para viagens de ate 200 km
# e R$ 0,45/km para viagens mais longas.

dis = int(input('Qual a distância da viagem em km? '))
if dis <= 200:
    valor = float(dis * 0.5)
else:
    valor = float(dis * 0.45)
print('O valor da passagem é R$ {:.2f}'.format(valor))
