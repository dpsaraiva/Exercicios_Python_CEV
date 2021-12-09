#Desafio: Crie um programa que mostre na tela todos os números pares entre 1 e 50.

print('Os números pares entre 1 e 50 são:')
for c in range(2, 51, 2):
    if c < 49:
        print(c, end= ', ')
    else:
        print(f'e {c}')
