soma = 0
for c in range(1, 7):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        soma += num
print('A soma dos valores pares é {}'.format(soma))
