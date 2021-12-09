#Desafio: Crie um programa onde o usuário possa digitar 7 valores numéricos, e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

geral =[[], []]
for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        geral[0].append(num)
    else:
        geral[1].append(num)
geral[0].sort()
geral[1].sort()
print(f'Os valores pares digitados foram: {geral[0]}')
print(f'Os valores ímpares digitados foram: {geral[1]}')
