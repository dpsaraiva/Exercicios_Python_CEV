#Desafio: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade(21) e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input('Qual o {}º ano? '.format(i))) + 21
    if ano >= ano_atual:
        maior += 1
    else:
        menor += 1
print('{} pessoa(s) atingiram a maioridade e {} pessoa(s) são menores de idade'.format(maior, menor))
