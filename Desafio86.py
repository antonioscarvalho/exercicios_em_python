l = []
p = []
i = []
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    l.append(n)
    if n % 2 == 0:
        p.append(n)
    elif n % 2 != 0:
        i.append(n)
print(f'''
A lista completa de números digitados ficou da seguinte maneira: {l}
A lista somente com números pares digitados: {p}
A lista somente com números impares digitados: {i}''')