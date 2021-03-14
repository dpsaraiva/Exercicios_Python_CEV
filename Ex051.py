prim_termo = int(input('Qual o primeiro termo dessa dessa PA? '))
razao = int(input('Qual a razão dessa PA? '))
ult_termo = prim_termo + 10 * razao
print('Os dez primeiros termos são:')
for c in range(prim_termo, ult_termo, razao):
    print(c)
