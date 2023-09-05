n = 0
p = 0
s = 0
c = 0
l = []
while True:
    print('''
Digite o nome do produto que deseja adquirir e o preço dele:
          ''')
    n = str(input('NOME: '))
    p = float(input('PREÇO: '))
    s = s + p
    if p > 1000:
        c = c + 1
    l.append(p)
    x = l[:]
    z = min(x)
    a = str(input('Quer continuar a adicionar produtos? [S/N] ')).upper().lstrip().rstrip()
    if a == 'N':
        break
print(f'''
      O total de gastos ficou no valor de R${s:.2f}.
      {c} produtos custam mais de R$1000,00
      O menor preço foi R${z:.2f}.''')