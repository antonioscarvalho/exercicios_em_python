t = ('lápis', 1
     , 'borracha', 2
     , 'caneta', 1
     , 'tesoura', 5
     , 'cola', 5)
for c in range(0, len(t)):
    if c % 2 == 0:
        print(f'Produto: {t[c]:.<20}', end = ' ')
    else:
        print(f'R${t[c]:.2f}')