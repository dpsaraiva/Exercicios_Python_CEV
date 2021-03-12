n1 = float(input('Qual a altura da parede em metros? '))
n2 = float(input('Qual a largura da parede em metros? '))
area = n1*n2
litros = area/2
print('A sua área é {:.2f} m2\nSão necessários {:.1f} litros de tinta'.format(area, litros))
