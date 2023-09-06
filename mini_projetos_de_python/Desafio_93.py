d = {}
d['nome'] = str(input('Qual o nome da pessoa? '))
a = int(input('Qual o ano de nascimento? '))
i = 2023 - a
d['idade'] = i
d['CTPS'] = str(input('Qual o número da sua CTPS? (0, caso não tenha) '))
if d['CTPS'] != '0':
    d['contratação'] = int(input('Qual o ano de contratação do seu trabalho? '))
    d['salário'] = float(input('Qual o seu salário? R$'))
    aposen = ((d['contratação'] + 35) - 2023) + i
    d['aposentadoria'] = aposen
else:
    print('Não possui Carteira de Trabalho.')
r = d.items()
for c, v in enumerate(r):
    print(f'O(a) {v[0]} recebeu o valor {v[1]}')