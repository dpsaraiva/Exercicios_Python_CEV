vel = int(input('Qual a velocidade do veículo? '))
if vel > 80:
    multa = float((vel - 80)*7)
    print('Sua velocidade é {}km/h. Você foi multado em R$ {:.2f}'.format(vel, multa))
else:
    print('Velocidade Permitida')
