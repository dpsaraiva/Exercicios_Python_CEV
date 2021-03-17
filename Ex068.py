from random import randint
cont = 0
while True:
    comp = randint(1, 10)
    num = ''
    while num.isnumeric() == False:
        num = input('Escolha um número: ')
    escolha = 'a'
    while escolha not in 'IP':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    soma = comp + int(num)
    if soma % 2 == 0 and escolha == 'P':
        print(f'O computador jogou {comp} e você {num}. Total {soma} DEU PAR ')
    elif soma % 2 == 0 and escolha == 'I':
        print(f'O computador jogou {comp} e você {num}. Total {soma} DEU PAR ')
        break
    elif soma % 2 != 0 and escolha == 'P':
        print(f'O computador jogou {comp} e você {num}. Total {soma} DEU ÍMPAR ')
        break
    else:
        print(f'O computador jogou {comp} e você {num}. Total {soma} DEU ÍMPAR ')
    print('Você VENCEU!!!')
    print('Vamos jogar novamente...')
    print('=-' * 20)
    cont += 1
print('Você PERDEU')
print('=-' * 20)
print(f'GAMER OVER! Você venceu {cont} vezes.')
