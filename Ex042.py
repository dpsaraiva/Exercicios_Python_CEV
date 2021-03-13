a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
if a + b > c and a + c > b and b + c > a:
    if a == b != c or a == c != b or b == c != a:
        print('Com os valores dado é possível formar um triângulo Isósceles!')
    elif a == b == c:
        print('Com os valores dado é possível formar um triângulo Equilátero!')
    else:
        print('Com os valores dado é possível formar um triângulo Escaleno!')
else:
    print('Não é possível formar um triângulo com esses valores!')
