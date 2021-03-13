from random import choice
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
jogador = input('Escolha pedra, papel ou tesoura: ').lower()
if jogador == 'pedra' and computador == 'tesoura' or jogador == 'papel' and computador == 'pedra' or jogador == 'tesoura' and computador == 'papel':
    print('O computador escolheu {}. Você GANHOU!!!'.format(computador))
elif jogador == computador:
    print('O computador escolheu {}. EMPATOU!!!'.format(computador))
else:
    print('O computador escolheu {}. Você PERDEU!!!'.format(computador))
