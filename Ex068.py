from random import randint
cont = 0
res = ''
while res != 'PERDEU':
    comp = randint(1, 10)
    num = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    soma = comp + num
    if soma % 2 == 0 and escolha == 'P':
        print(f'O computador jogou {comp} e você {num}. Total de {soma} DEU PAR ')
    elif soma % 2 == 0 and escolha == 'I':
        print(f'O computador jogou {comp} e você {num}. Total de {soma} DEU PAR ')
        break
    elif soma % 2 != 0 and escolha == 'P':
        print(f'O computador jogou {comp} e você {num}. Total de {soma} DEU ÍMPAR ')
        break
    else:
        print(f'O computador jogou {comp} e você {num}. Total de {soma} DEU ÍMPAR ')
    print('Você VENCEU')
    print('Vamos jogar novamente...')
    print('=-' * 20)
    cont += 1
print('Você PERDEU')
print('=-' * 20)
print(f'GAMER OVER! Você venceu {cont} vezes.')