pessoa = {}
cadastros = []
media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    cadastros.append(pessoa.copy())
    continua = input('Deseja cadastrar mais? [S/N] ').upper().strip()[0]
    if continua == 'N':
        break
for i in range(0, len(cadastros)):
    media += cadastros[i]['idade']
media = media/len(cadastros)
print('=-' * 30)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas')
print(f'B) A média de idade é de {media} anos')
print('C) As mulheres cadastradas foram ', end=' ')
for i in range(0, len(cadastros)):
    if cadastros[i]['sexo'] in 'Ff':
        print(cadastros[i]['nome'], end=' ')
print('')
print('D) Listas das pessoa que estão acima da média:')
for i in range(0, len(cadastros)):
    if cadastros[i]['idade'] > media:
        print(f'     nome = {cadastros[i]["nome"]}; sexo = {cadastros[i]["sexo"]}; idade = {cadastros[i]["idade"]}')
