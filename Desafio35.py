sal = float(input('Qual o seu salário? R$'))
aumsup = sal * 0.10
sup = sal + (aumsup)
auminf = sal * 0.15
inf = sal + (auminf)
if sal > 1250.00:
    print('Seu salário recebeu um aumento de 10%, ou seja, de R${0:.2f}. Portanto, seu novo salário é R${1:.2f}.'.format(aumsup, sup))
else:
    print('Seu salário recebeu um aumento de 15%, ou seja, de R${0:.2f}. Portanto, seu novo salário é R${1:.2f}.'.format(auminf, inf))