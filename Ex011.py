#Desafio: Faça um programa que leia a altura e a largura de uma parede em metros, calcule
#a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
#pinta uma área de 2m².

n1 = float(input('Qual a altura da parede em metros? '))
n2 = float(input('Qual a largura da parede em metros? '))
area = n1*n2
litros = area/2
print('A sua área é {:.2f} m2\nSão necessários {:.1f} litros de tinta'.format(area, litros))
