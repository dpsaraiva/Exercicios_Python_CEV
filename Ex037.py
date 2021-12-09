#Desafio: Escreva um programa que leia um número inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão:
#1 para binário;
#2 para octal;
#3 para hexadecimal.

num = int(input('Digite um numero qualquer: '))
print('Escolha a base de conversão:\n'
      'Digite 1 para binário;\n'
      'Digite 2 para octal;\n'
      'Digite 3 para hexadecimal.')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido em OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção INVÁlIDA. Tente novamente.')
