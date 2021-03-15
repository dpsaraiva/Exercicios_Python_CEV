num = int(input('Digite um número inteiro: '))
num1 = num
res = num
while res > 1:
    num = num * (res - 1)
    res = res - 1
print('O fatorial de {} é {}'.format(num1, num))
