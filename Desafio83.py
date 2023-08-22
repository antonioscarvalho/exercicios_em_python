l = []
p = []
i = []
r = 0
while r != 'N':
    n = int(input('Digite um número: '))
    l.append(n)
    if n % 2 == 0:
        p.append(n)
    elif n % 2 != 0:
        i.append(n)
    r = str(input('Você continuar a escrever números? [S/N] ')).lstrip().rstrip().upper()
print(f'''
A lista completa ficou da seguinte forma: {l}
A lista de números pares: {p}
A lista de números impares: {i}
E o conteúdo dessas três listas acima juntas ficou da seguinte forma: {l+p+i}''')
    