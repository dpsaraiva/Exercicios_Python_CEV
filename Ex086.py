matriz = [[], [], []]
for n in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite um valor para[{n}, {i}]: '))
        matriz[n].append(num)
print('=-' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')
