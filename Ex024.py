texto = input('Qual o nome da sua cidade? ')
texto = texto.lstrip()
texto = texto.capitalize()
res = 'Santo'in texto
print('O nome da cidade começa com Santo?', res)
