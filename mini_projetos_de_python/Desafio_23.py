#Manipulação de textos
nome = str(input('Digite seu nome completo: '))
maius = nome.upper()
minus = nome.lower()
sespaco = nome.replace(' ','')
contadorcaractere = len(sespaco)
sep = nome.split()
primnome = len(sep[0])
print('O seu nome com todas as letras maiúsculas fica da seguinte forma: {0}; Com minúsculas: {1}; A quantidade de letras nele é: {2}; E a quantidade de letras que tem seu primeiro nome é: {3}.'.format(maius, minus, contadorcaractere, primnome))