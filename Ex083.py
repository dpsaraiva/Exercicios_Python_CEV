num = list
num = input('Digite a expressão: ')
if num.count('(') == num.count(')'):
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada!')
