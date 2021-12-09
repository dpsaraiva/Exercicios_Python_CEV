#Desafio: Faça um programa que tenha uma função chamada ficha(), que receba dois parmetros opcionais:
#O nome de um jogador e quantos gols ele marcou. O progama deverá ser capaz de mostrar a ficha do jogador,
#mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


#Programa Principal
jogador = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)
