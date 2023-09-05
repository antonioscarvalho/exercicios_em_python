l = []
c = 0
n = 0
while n != 'N':
    l.append(int(input('Digite um valor: ')))
    c = c + 1
    n = str(input('Quer continuar? [S/N] ')).upper().lstrip().rstrip()
s = set(l)
print(f'Os valores digitados sem duplicatas em ordem crescente: {s}')