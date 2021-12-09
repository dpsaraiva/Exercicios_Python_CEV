#Desafio: Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. 

from random import randint
num_pc = randint(0, 10)
cont = 1
num_usu = int(input('Escolha um número de 0 a 10: '))
while num_usu != num_pc:
    if num_usu > num_pc:
        num_usu = int(input('Menos...Tente novamente: '))
    else:
        num_usu = int(input('Mais... Tente novamente: '))
    cont += 1
if cont > 1:
    print('PARABÉNS!!! Você acertou depois de {} tentativas'. format(cont))
else:
    print('PARABÉNS!!! Você acertou na 1ª tentativa')
