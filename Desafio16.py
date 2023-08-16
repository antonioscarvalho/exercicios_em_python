#Aluguel de Carros
km = float(input('Informe a quantidade de Km rodados: '))
dias = int(input('Informe a quantidade de dias que foram passados durante o aluguel: '))
taxakm = km * 0.15
taxadia = dias * 60
total = taxakm + taxadia
print('O aluguel do carro custou R${0:.2f}.'.format(total))