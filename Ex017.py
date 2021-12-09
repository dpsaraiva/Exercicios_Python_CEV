#Desafio:Faça um programa que leia o comprimento de um cateto oposto e de um cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hiponetunsa.

import math
c1 = float(input('Valor do primeiro cateto: '))
c2 = float(input('Valor do segundo cateto: '))
hip = float(math.hypot(c1, c2))
print('A hipotenusa mede {:.1f}'.format(hip))
