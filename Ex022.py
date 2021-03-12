nome = input('Qual seu nome completo? ')
# Nome em maiúculo
print(nome.upper())

# Nome em minúsculo
print(nome.lower())

# Tamanho do nome sem espaços
print(len(nome.replace(' ','')))

# Tamanho do primeiro nome
primeiro_nome = nome.split()
print(len(primeiro_nome[0]))
