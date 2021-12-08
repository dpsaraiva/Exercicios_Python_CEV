#Desafio: Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input('Informe a temperatura em Celsius (ºC)? '))
f = c*1.8 + 32
print("A temperatura em Fahrenheit é {:.1f}ºF".format(f))
