#Essa frase é um palíndromo?
fr = str(input('Digite algo para ver se é ou não um palíndromo: ')).lower()
plv = fr.split()
j = ''.join(plv)
i = ''
for c in range(len(j) - 1, -1, -1):
    i = i + j[c]
if i == j:
    print('Palíndromo.')
else:
    print('Não é.')