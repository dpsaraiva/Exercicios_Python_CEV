#Desafio: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá 
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos. 

maior18 = mulheres = homens = 0
while True:
    idade = int(input('Qual a sua idade? '))
    if idade > 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Qual o seu sexo?[M/F] ').upper().strip()[0]
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M':
        homens += 1
    continua = ' '
    while continua not in 'SN':
        continua = input('Deseja continuar cadastrando?[S/N] ').upper().strip()[0]
    if continua == 'N':
        break
    print('=-' * 20)
print('Foram cadastrados {} homens; {} pessoas têm mais de 18 anos e {} mulheres abaixo de 20 anos'.format(homens, maior18, mulheres))
