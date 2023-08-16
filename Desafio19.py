#OPERAÇÕES
import math
ang = int(input('Digite o valor de um ângulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('O valor do seno é {0:.2f}, do cosseno é {1:.2f} e da tangente é {2:.2f}.'.format(sen, cos, tan))