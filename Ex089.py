alunos = []
nome = list()
notas = []
media = []
while True:
    nome.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media.append((notas[0]+notas[1])/2)
    nome.append(notas[:])
    alunos.append(nome[:])
    nome.clear()
    notas.clear()
    cont = input('Deseja continuar? S/N ').upper().strip()[0]
    if cont in 'Nn':
        break
for i in range(0, len(alunos)):
    print(f'{i + 1:<5} {alunos[i][0]:^15} {media[i]:>4.1f}')

while True:
    aluno = int(input('Mostrar as notas de qual aluno? (999 para sair) '))
    if aluno == 999:
        break
    print(f'As notas de {alunos[aluno - 1][0]} são {alunos[aluno - 1][1]} ')
