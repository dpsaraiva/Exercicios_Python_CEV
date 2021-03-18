num = int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')), int(input('Digite o último valor: '))
num3 = 5
for cc in range(0, len(num)):
    if num[cc] == 3:
        num3 = f'O numero 3 apareceu na {num.index(3) + 1}ª posição'
    if num3 == 5:
        num3 = 'O número 3 não foi digitado'
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
print(num3)
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
