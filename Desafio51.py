print('TABUADA')
n = int(input('Digite o número para fazer a tabuada dele: '))
for c in range(1, 11):
    x = n * c
    print('{0} x {1} = {2}'.format(n, c, x))