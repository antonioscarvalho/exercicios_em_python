ano = int(input('Digite o número do ano que você nasceu: '))
idade = int(2023 - ano)
qaf = int(18 - idade)
qap = int(idade - 18)
if idade < 18:
    print('Fique tranquilo, você só terá que se alistar daqui a {0} ano(s).'.format(qaf))
elif idade == 18:
    print('Já está na hora de se alistar. Realize já o seu alistamento militar.')
else:
    print('Você já deveria ter feito seu alistamento militar a {0} ano(s).'.format(qap))
