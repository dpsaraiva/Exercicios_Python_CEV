#Desafio: Crie um pacote chamado utilidadesCeV que tenha dois módulos moeda e dado.
#Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadecev import moedas
p = float(input('Digite o preço: R$ '))
moedas.resumo(p, 80, 35)
