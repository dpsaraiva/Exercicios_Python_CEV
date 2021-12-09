#Desafio:Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário descobrir qual foi o número escolhido pelo computador.
#O programa deverá informar na tela se o usuário venceu ou perdeu.

from random import randrange

num_pc = randrange(6)
num_usu = int(input('Qual número o computador escolheu de 0 a 5? '))
if num_pc == num_usu:
    print('Parabéns você acertou!!!')
else:
    print('Voce errou, o computador escolheu {}'.format(num_pc))


