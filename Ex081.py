#Desafio: Crie um programa quue vai ler vários números e colocar em uma lista. Depois disso mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

num = list()
while True:
    num.append(int(input('Digite um número: ')))
    continua = input('Quer continuar: [S/N]').upper().strip()[0]
    if continua == 'N':
        break
num.sort(reverse=True)
print('-=' * 40)
print(f'Você digitou {len(num)} números')
print(f'Os valores em ordem decrescente são {num}')
if num.count(5):
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado')
