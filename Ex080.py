#Desafio: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de insersão(sem usar o sort()).
# No final mostre a lista ordenada na tela.

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
