cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
if cont == 0:
    print('Nenhum número foi digitado')
elif cont == 1:
    print(f'Você digitou o número {soma}')
else:
    print(f'Você digitou {cont} números com soma igual a {soma}')