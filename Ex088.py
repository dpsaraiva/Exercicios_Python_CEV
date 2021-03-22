from random import randint, sample
from time import sleep
jogos = int(input('Quantos jogos deseja gerar? '))
for j in range(0, jogos + 1):
    palpites = sample(range(1, 61), k=6)
    palpites.sort()
    print(f'Jogo {j}: {palpites}')
    sleep(0.5)
