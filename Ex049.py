#Desafio: Refaça o exercicio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número inteiro: '))
print('Sua tabuada é: ')
for c in range(0, 11):
    res = num * c
    print('{} x {} = {}'.format(num, c, res))
