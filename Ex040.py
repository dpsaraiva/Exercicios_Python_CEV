nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('\033[1;31mReprovado\033[m')
elif media >= 5 and media < 6.9:
    print('\033[1;33mRecuperação\033[m')
else:
    print('\033[1;34mAprovado\033[m')
