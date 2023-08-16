c = 1
r = 1
n = int(input('Digite um número e veja seu fatorial: '))
while c <= n:
    r = r * c
    c = c + 1
print('O resultado do fatorial de {0} é: {1}.'.format(n, r))