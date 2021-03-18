turpla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
          'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
pal = ''
print('')
for pos in turpla:
    pal = pos
    print(f' Na palavra {pal} temos', end=' ')
    for cont in range(0, len(pal)):
        if pal[cont] == 'A':
            print('a', end=' ')
        if pal[cont] == 'E':
            print('e', end=' ')
        if pal[cont] == 'I':
            print('i', end=' ')
        if pal[cont] == 'O':
            print('o', end=' ')
        if pal[cont] == 'U':
            print('u', end=' ')
    print('')
