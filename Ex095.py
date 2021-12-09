#Desafio: Aprimore o Desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

ficha = {}
gols = []
geral = []
while True:
    gols.clear()
    ficha['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {ficha["Nome"]} jogou: '))
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {p + 1}ª partida: ')))
    ficha['Gols'] = gols[:]
    ficha['Total'] = sum(gols)
    geral.append(ficha.copy())
    while True:
        resp = input('Quer continuar? [S/N]').upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO. Digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 27)
print('cod', end=' ')
for i in ficha.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 50)
for k, v in enumerate(geral):
    print(f'{k + 1:<3}', end=' ')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
while True:
    print('-' * 50)
    dados = int(input('Mostrar dados de qual jogador? (999 para sair) ')) - 1
    if dados == 998:
        break
    if dados >= len(geral):
        print(f'ERRO! Não existe jogador com código {dados + 1}')
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR: {geral[dados]['Nome']}")
        for i, g in enumerate(geral[dados]['Gols']):
            print(f"Na {i + 1}ª partida fez {g} gols")
print('     ----ENCERRADO----')
