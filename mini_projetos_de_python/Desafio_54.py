n = int(input('Escreva um número para verificar se ele é ou não primo: '))
cont = 0
for c in range(2, n):
    if n % c == 0:
        print('Multiplo de {}.'.format(c))
        cont = cont + 1
if cont == 0:
    print('É primo.')
else:
    print('Não é primo.')

