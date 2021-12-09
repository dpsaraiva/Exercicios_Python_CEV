#Desafio: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Pão', 1.00, 'Leite', 4.00, 'Biscoito', 4.50, 'Macarrão', 3.50, 'Queijo', 30.00, 'Arroz', 30.00, 'Feijão', 20.00, 'Café', 12.00)
print('-' * 51)
print(f'{"LISTAGEM DE PREÇOS":^51}')
print('-' * 51)
for n in range(0, len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<42}', end='')
    else:
        print(f' R$ {lista[n]:>5.2f}')
print('-' * 51)
