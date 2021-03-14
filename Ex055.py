maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Qual o {}º peso? '.format(i)))
    if peso > maior:
        maior = peso
        menor = maior
    if menor > peso:
        menor = peso
print('O maior peso é {:.1f} kg'.format(maior))
print('O menor peso é {:.1f} kg'.format(menor))
