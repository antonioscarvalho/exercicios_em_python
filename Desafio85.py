l = []
c = 0
ma = []
me = []
ma1 = []
me1 = []
a = 0
while a != 'N':
    n = str(input('Qual o nome? '))
    l.append(n)
    p = float(input('Qual o peso? '))
    l.append(p)
    c = c + 1
    a = str(input('Deseja adicionar mais pessoas? [S/N] ')).upper().lstrip().rstrip()
    if p > 100:
        ma.append(n)
        ma1.append(p)
    elif p < 100:
        me.append(n)
        me1.append(p)
x = max(ma1)
y = min(me1)
print(f'''
    {c} pessoa(s) foram adicionada(s).
    Lista de pessoas com peso acima de 100,00kg: {ma}. O maior dos pesos: {x:.2f}kg.
    Lista de pessoas com peso abaixo de 100,00kg: {me}. O menor dos pesos: {y:.2f}kg.
    ''')


