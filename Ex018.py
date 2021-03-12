import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O valor do sen de {} é {:.2f}'.format(ang, sen))
print('O valor do cos de {} é {:.2f}'.format(ang, cos))
print('O valor da tan de {} é {:.2f}'.format(ang, tan))

