#Desafio: Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    res = larg * comp
    print(f'A área de um terreno {larg} x {comp} é {res}m²')


print('Controle dos Terrenos')
print('==' * 20)
a = float(input('LARGURA(m²): '))
b = float(input('COMPRIMENTO(m²): '))
area(a, b)
