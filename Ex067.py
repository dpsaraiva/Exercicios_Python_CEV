#Desafio: Faça um programa que mostre a tabuada de vários númeoros, um de cada vez, para cada valor digitado pelo usúario.
# O programa será interrompido quando o número solicitado for negativo. 

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('--' * 18)
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('--' * 18)
print('==' * 17)
print('PROGRAMA ENCERRADO')
