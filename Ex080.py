num = []
for cont in range(0, 5):
    aux = int(input('Digite um valor: '))
    if cont == 0 or aux > num[-1]:
        num.append(aux)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if aux <= num[pos]:
                num.insert(pos, aux)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(num)
