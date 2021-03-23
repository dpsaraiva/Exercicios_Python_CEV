from random import sample
from time import sleep
jogos = int(input('Quantos jogos deseja gerar? '))
for j in range(0, jogos):
    palpites = sample(range(1, 61), k=6)
    palpites.sort()
    print(f'Jogo {j + 1}: {palpites}')
    sleep(0.7)
