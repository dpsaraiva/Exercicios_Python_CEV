#Desafio: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados em ordem correta.

num = list
num = input('Digite a expressão: ')
if num.count('(') == num.count(')'):
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada!')
