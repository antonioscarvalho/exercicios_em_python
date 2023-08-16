c = 0
n = 0
while n >= 0:
    n = int(input('Digite o número para fazer a tabuada dele: '))
    for c in range(1, 11):
        x = n * c
        if n >= 0:
            print('{0} x {1} = {2}'.format(n, c, x))
        else:
            break
print('Se digitar um negativo, o programa acaba.')