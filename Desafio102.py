from random import randint
numeros = []
def sorteia():
    for c in range(0, 5):
        n = randint(1, 9)
        numeros.append(n)

sorteia()
print(f'A lista de valores sorteados foi: {numeros}')

par = []
def somaPar():
    for c in range(0,5):
        if numeros[c] % 2 == 0:
            par.append(numeros[c])

somaPar()
print(f'Os valores pares dessa lista são: {par}')
print(f'A soma desses valores é: {sum(par)}')

