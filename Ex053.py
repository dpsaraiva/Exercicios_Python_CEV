frase = input('Digite uma frase ou palavra: ').lower().replace(' ', '')
frase2 = ''
tamanho = len(frase)
for c in range(tamanho - 1, -1, -1):
    frase2 += frase[c]
if frase == frase2:
    print('A frase\palavra é palíndromo')
else:
    print('a frase\palavra não é palíndromo')
