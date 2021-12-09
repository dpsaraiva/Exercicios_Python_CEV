#Desafio: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo;
# Qual é o homem mais velho;
# quantas mulheres têm menos de 20 anos.

somaidade = 0
maioridadehomem = 0
nomevelho = ''
media = 0
totmulher = 0
for i in range(1, 5):
    print('Dados da {}ª Pessoa'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo M/F: ').lower().strip()
    print('==' * 20)
    somaidade += idade
    if i == 1 and sexo == 'm':
        maioridadehomem = idade
        nomevelho = nome
    if idade > maioridadehomem and sexo == 'm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'f' and idade < 25:
        totmulher += 1
media = somaidade / 4
print('A média das idades é {:.1f} anos'.format(media))
print('O homem mais velho é {} com {} anos.'.format(nomevelho, maioridadehomem))
print('{} mulher(es) tem menos de 20 anos'.format(totmulher))
