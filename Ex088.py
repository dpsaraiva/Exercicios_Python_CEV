#Desafio: Faça um programa que ajude um jogador da MEGASENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
from time import sleep
jogos = int(input('Quantos jogos deseja gerar? '))
for j in range(0, jogos):
    palpites = sample(range(1, 61), k=6)
    palpites.sort()
    print(f'Jogo {j + 1}: {palpites}')
    sleep(0.7)
