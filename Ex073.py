#Desafio: Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol 2019, na ordem de colocação. Depois Mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time "Chapecoense" 

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
         'Santos', 'Atlético-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife',
         'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Classificação Brasileirão 2020: {times}')
print(f'Os 5 primeiros colocados {times[:5]}')
print(f'Os 4 últimos colocados {times[-4:]}')
print(f'Os times em ordem alfabética{sorted(times)}')
print(f'O Ceará aparece em {times.index("Ceará") + 1}º na tabela')

