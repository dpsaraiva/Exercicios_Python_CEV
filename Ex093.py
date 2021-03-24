ficha = {}
gols = []
ficha['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {ficha["Nome"]} jogou: '))
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {p + 1}ª partida: ')))
ficha['Gols'] = gols
ficha['Total'] = sum(gols)
print('-=' * 30)
for k, v in ficha.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'O jogagor {ficha["Nome"]} jogou {partidas} partidas:')
for k, v in enumerate(gols):
    print(f'  => Na partida {k + 1}, fez {v} gols')
print(f'Foi um total de {ficha["Total"]}')
