sexo = input('Digite seu sexo no formato [M] ou [F]: ').strip().upper()[0]
while sexo != 'F' and sexo != 'M':
    sexo = input('Valor invalído. Digite novamente: ').strip().upper()[0]
if sexo == 'F':
    sexo = 'FEMININO'
else:
    sexo = 'MASCULINO'
print('Sexo {} registrado com sucesso.'.format(sexo))

