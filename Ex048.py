#Desafio: Faça um programa que calcule a soma entre todos os números impares que 
#são múltiplos de três e que se encontrem no intervalo de 1 até 500.

s = 0
for c in range(0, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print('A soma de todos números ímpares divisíveis por 3 de 0 a 500 é: {}'.format(s))
