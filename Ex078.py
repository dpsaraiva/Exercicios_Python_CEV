#Desafio: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = list()
posmaior = list()
for n in range(0, 5):
    num.append(int(input(f'Digite um valor para a Posição {n}: ')))
print('-=' * 25)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} nas posições', end=' ')
for c, v in enumerate(num):
    if max(num) == v:
        print(f'{c}...', end=' ')
print(f'\nO menor valor digitado foi {min(num)} nas posições', end=' ')
for c, v in enumerate(num):
    if min(num) == v:
        print(f'{c}...', end=' ')
