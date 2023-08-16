#OPERAÇÕES
larg = int(input('Digite a largura em metros: '))
h = int(input('Digite a altura em metros: '))
area = larg * h
#1l de tinta pinta 2m²
tinta = area / 2
print('Sua parede tem uma área de {0}m² e é preciso de {1:.1f}l de tinta para pintá-la.'.format(area, tinta))