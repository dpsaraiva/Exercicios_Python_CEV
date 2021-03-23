dados = dict()
dados['nome'] = str(input('Nome do aluno: '))
dados['media'] = float(input(f'Qual a sua média {dados["nome"]}: '))
if dados['media'] < 5:
    situacao = 'Reprovado'
elif dados['media'] < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Aprovado'
dados['situacao'] = situacao
print('=-' * 20)
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
print(f'Situacao é igual a {dados["situacao"]}')
