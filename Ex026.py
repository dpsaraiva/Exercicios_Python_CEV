#Desafio:Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'.
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

frase = input('Escreva uma frase: ')
frase = frase.upper()
a = frase.count("A")
primeiravez = frase.find('A')
ultimavez = frase.rfind('A')
print('A letra "a" aparece {} vezes na frase'.format(a))
print('A primeira vez que ela aparece é na posição {}'.format(primeiravez))
print('A ultima vez que ela aparece é na posição {}'.format(ultimavez))
