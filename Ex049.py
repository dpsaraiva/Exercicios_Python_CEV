num = int(input('Digite um número inteiro: '))
print('Sua tabuada é: ')
for c in range(0, 11):
    res = num * c
    print('{} x {} = {}'.format(num, c, res))
