a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
if a + b > c and a + c > b and b + c > a:
    print('Com os valores dados é possível formar um triângulo')
else:
    print('Não é possivel formar um triângulo com esses valores')
