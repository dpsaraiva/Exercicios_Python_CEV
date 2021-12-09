#Desafio: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final. mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
while True:
    nome = str(input('Nome: '))
    notas1 = float(input('Nota 1: '))
    notas2 = float(input('Nota 2: '))
    media = (notas1+notas2)/2
    alunos.append([nome, [notas1, notas2], media])
    cont = input('Deseja continuar? S/N ').upper().strip()[0]
    if cont in 'Nn':
        break
for i in range(0, len(alunos)):
    print(f'{i + 1:<5} {alunos[i][0]:^15} {alunos[i][2]:>4.1f}')
while True:
    aluno = int(input('Mostrar as notas de qual aluno? (999 para sair) '))
    if aluno == 999:
        break
    print(f'As notas de {alunos[aluno - 1][0]} são {alunos[aluno - 1][1]} ')
