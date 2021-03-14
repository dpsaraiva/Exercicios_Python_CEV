num = int(input('Digite um número inteiro: '))
primo = 0
if num < 2:
    print('O número não é primo')
else:
    for c in range(2, num):
        if num % c == 0:
            primo += 1
    if primo > 0:
        print('O número não é primo')
    else:
        print('O número é primo')
