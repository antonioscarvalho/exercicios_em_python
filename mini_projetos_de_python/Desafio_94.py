d = {}
l = []
print('''Aproveitamento de um Jogador:
''')
d['nome'] = str(input('Qual o nome do jogador? '))
part = int(input('Quantas partidas de futebol ele jogou? '))
if part != 0:
    for c in range(0, part):
        g = int(input(f'Quantos gols na {c+1}° partida? '))
        l.append(g)
else:
    print('Não jogou nenhuma partida.')   
d['gols'] = l
d['total'] = sum(l)
print(f'''
{d}
''')

for c, v in d.items():
    print(f'O campo {c} foi preenchido com {v}.')

print(f'''
O jogador {d["nome"]} jogou {part} partidas:''')
for c in range(0, part):
    print(f'-> Na {c+1}° partida fez {l[c]} gols.')
print(f'Ou seja, foi um total de {d["total"]} gols.')
