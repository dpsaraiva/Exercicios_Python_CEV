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
