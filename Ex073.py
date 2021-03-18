times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
         'Santos', 'Atlético-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife',
         'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Classificação Brasileirão 2020: {times}')
print(f'Os 5 primeiros colocados {times[:5]}')
print(f'Os 4 últimos colocados {times[-4:]}')
print(f'Os times em ordem alfabética{sorted(times)}')
print(f'O Ceará aparece em {times.index("Ceará") + 1}º na tabela')

