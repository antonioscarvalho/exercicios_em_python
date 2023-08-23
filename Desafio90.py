b = list()
while True:
    nome = str(input('Qual o nome do aluno? '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    x = ((n1 + n2)/2)
    b.append([nome, [n1, n2], x])
    r = str(input('Quer continuar? [S/N] ')).upper().rstrip().lstrip()
    if r == 'N':
        break
print('N°   Nome:        Média:')
for i, a in enumerate(b):
    print(f'''{i+1}    {a[0]:<13}{a[2]:.1f}''')