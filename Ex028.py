from random import randrange

num_pc = randrange(6)
num_usu = int(input('Qual número o computador escolheu de 0 a 5? '))
if num_pc == num_usu:
    print('Parabéns você acertou!!!')
else:
    print('Voce errou, o computador escolheu {}'.format(num_pc))


