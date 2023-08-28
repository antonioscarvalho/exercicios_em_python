d = {}
d['nome'] = str(input('Qual o nome do aluno? '))
d['nota média'] = float(input(f'Qual a nota de {d["nome"]}? '))
if d['nota média'] >= 7:
    print(f'''
O {d["nome"]} está aprovado, visto que sua nota foi {d['nota média']:.1f}, estando acima da média.''')
else:
    print(f'''
O {d["nome"]} está reprovado, visto que sua nota foi {d['nota média']:.1f}, estando abaixo da média.''')

