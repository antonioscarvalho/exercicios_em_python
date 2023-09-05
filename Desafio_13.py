#OPERAÇÕES
n = float(input('Qual o preço do produto? R$'))
desc = n - (n * 0.05)
print('O preço do produto com 5% de desconto é R${0:.2f}.'.format(desc))