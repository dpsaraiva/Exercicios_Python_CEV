#Desafio: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
#R$ 60,00 por dia e R$ 0,15 por Km rodado.

d = int(input('Dias de locação do veículo: '))
k = int(input('Quantos km rodados? '))
p = float(d * 60 + 0.15 * k)
print('O total a pagar é de R${:.2f}'.format(p))
