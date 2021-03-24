from random import randint
from operator import itemgetter
from time import sleep
jogadores = {}
print('Valores Sorteados:')
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou o {v} no dado')
    sleep(1)
jogadores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=-' * 30)
for l, m in enumerate(jogadores):
    print(f'{l + 1}º lugar: {m[0]} com {m[1]}.')
    sleep(1)
