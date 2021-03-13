preco = float(input('Qual o preço do produto? '))
pagamento = int(input('Escolha a forma de pagamento:\n'
                            'Digite 1 para à vista dinheio/cheque;\n'
                            'Digite 2 para à vista no cartão;\n'
                            'Digite 3 para até 2x no cartão;\n'
                            'Digite 4 para 3x ou mais no cartão.\n'))
if pagamento == 1:
    print('Total R$ {:.2f} no dinheiro / cheque'.format(preco * 0.9))
elif pagamento == 2:
    print('Total R$ {:.2f} à vista no cartão'.format(preco * 0.95))
elif pagamento == 3:
    print('Total R$ {:.2f} em 2x no cartão'.format(preco))
else:
    print('Total R$ {:.2f} em 3x ou mais no cartão'.format(preco * 1.2))
