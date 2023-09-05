#Manipulação de textos
n = int(input('Digite um número de 0 a 9999: '))
uni = n % 10
numsuni = (n - uni)/10
dez = int(numsuni%10)
numsdez = (n - dez)/100
cen = int(numsdez%10)
numscen = (n - cen)/1000
milh = int(numscen%10)
print('Em seguida, é possível ver suas:')
print('unidade(s): {}.'.format(uni))
print('dezena(s): {}.'.format(dez))
print('centena(s): {}.'.format(cen))
print('milhar(s): {}.'.format(milh))