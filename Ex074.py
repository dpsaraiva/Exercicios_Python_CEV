from random import randint
a = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
maior = 0
menor = 0
for i in range(0, 5):
    if i == 0:
        menor = a[0]
    if a[i] > maior:
        maior = a[i]
    if a[i] < menor:
        menor = a[i]
print(f'Os valores sorteados foram {a}')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')

