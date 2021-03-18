numext = ('zero', 'um', 'dois', 'três', 'quatro,',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num >= 0 and num < 21:
        break
    print('NÚMERO INVÁLIDO')
print(f'Você digitou o número {numext[num]}')
