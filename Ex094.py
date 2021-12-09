#Desafio: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
#de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas;
#B) A média de idade do grupo;
#C) Uma lista com todas as mulheres;
#D) Uma lista com todas as pessoas com idade acima da média.

pessoa = {}
cadastros = []
media = soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastros.append(pessoa.copy())
    while True:
        continua = input('Deseja cadastrar mais? [S/N] ').upper().strip()[0]
        if continua in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if continua == 'N':
        break
media = soma/len(cadastros)
print('=-' * 30)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas')
print(f'B) A média de idade é de {media:.1f} anos')
print('C) As mulheres cadastradas foram ', end=' ')
for i in range(0, len(cadastros)):
    if cadastros[i]['sexo'] in 'Ff':
        print(cadastros[i]['nome'], end=' ')
print()
print('D) Listas das pessoa que estão acima da média:')
for i in range(0, len(cadastros)):
    if cadastros[i]['idade'] > media:
        print(f'     nome = {cadastros[i]["nome"]}; sexo = {cadastros[i]["sexo"]}; idade = {cadastros[i]["idade"]}')
print('.....ENCERRADO......')
