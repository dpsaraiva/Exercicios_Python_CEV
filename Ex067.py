num = 0
while num >= 0:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 18)
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
print('==' * 17)
print('Programa encerrado')
