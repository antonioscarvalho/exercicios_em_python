nome = str(input('Digite seu nome: '))
sep = nome.split()
pri = sep[0]
ult = sep[-1]
print('Seu primeiro nome é {0} e seu último nome é {1}, certo?'.format(pri, ult))