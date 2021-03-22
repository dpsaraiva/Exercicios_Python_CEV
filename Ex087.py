matriz = [[], [], []]
par = soma = maior = 0
for n in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite um valor para[{n}, {i}]: '))
        if num % 2 == 0:
            par += num
        if i == 2:
            soma += num
        if n == 1 and num > maior:
            maior = num
        matriz[n].append(num)
print('=-' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')
print('=-' * 25)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
