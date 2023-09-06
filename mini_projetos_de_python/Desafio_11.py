#Ler a quantidade de reais e quantos dolares ela pode comprar, considerando o valor unitário do doĺar (US$1,00) como R$3,27
n = float(input('Quantos reais você tem em sua carteira? '))
dol = (n)/3.27
print('Você com esse dinheiro em reais que tem em sua carteira consegue comprar US${0:.2f}.'.format(dol))