val = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário do possível comprador? R$'))
ano = int(input('Em quantos anos quer pagar? '))
mes = ano * 12
prest = val/mes
if prest < (sal * 0.3):
    print('Você foi beneficiado com o empréstimo. As prestações mensais estarão no valor de R${0:.2f}.'.format(prest))
else:
    print('O empréstimo foi negado, visto que a prestação mensal está acima de 30% do salário do possível comprador.')