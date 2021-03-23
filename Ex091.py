from random import randint
jogadores = {}
print('Valores Sorteados:')
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou o {v} no dado')
print(jogadores)

