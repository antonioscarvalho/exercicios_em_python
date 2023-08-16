#OPERAÇÕES
import math
co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente: '))
hip = math.sqrt((co**2)+(ca**2))
print('O valor da hipotenusa é {0:.2f}.'.format(hip))