#Desafio: Faça um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lido. 

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Qual o {}º peso? '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if menor > peso:
            menor = peso
print('O maior peso é {:.1f} kg'.format(maior))
print('O menor peso é {:.1f} kg'.format(menor))
