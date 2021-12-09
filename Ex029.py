#Desafio:Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 para cada km acima do limite.

vel = int(input('Qual a velocidade do veículo? '))
if vel > 80:
    multa = float((vel - 80)*7)
    print('Sua velocidade é {}km/h. Você foi multado em R$ {:.2f}'.format(vel, multa))
else:
    print('Velocidade Permitida')
