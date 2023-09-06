kmviajados = int(input('Qual a quantidade de quilometros viajados: '))
p1 = (kmviajados * 0.5)
p2 = (kmviajados * 0.45)
if kmviajados <= 200:
    print('O preço da passagem calculada por km viajados foi: R${0:.2f}.'.format(p1))
else:
    print('O preço da passagem calculada por km viajados foi: R${0:.2f}.'.format(p2))