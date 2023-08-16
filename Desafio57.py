l = []
for c in range(0, 5):
    p = float(input('Digite o peso da pessoa: '))
    l.append(p)
    x = l[0:5]
y = max(x)
z = min(x)
print('O maior dos pesos é {} e o menor peso é {}.'.format(y, z))