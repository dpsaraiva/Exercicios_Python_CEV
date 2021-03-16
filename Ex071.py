valor = int(input('Qual valor você quer sacar? '))
nota50 = int(valor / 50)
sobra50 = valor - nota50 * 50
nota20 = int(sobra50 / 20)
sobra20 = sobra50 - nota20 * 20
nota10 = int(sobra20 / 10)
sobra10 = sobra20 - nota10 * 10
nota01 = sobra10
print('Total de {} cédulas de R$ 50.00'.format(nota50))
print('Total de {} cédulas de R$ 20.00'.format(nota20))
print('Total de {} cédulas de R$ 10.00'.format(nota10))
print('Total de {} cédulas de R$ 1.00'.format(nota01))