import random
from operator import itemgetter
print('Valores sorteados: ')
d = {'jogador 1':random.randint(1, 6),
     'jogador 2':random.randint(1, 6),
     'jogador 3':random.randint(1, 6),
     'jogador 4':random.randint(1, 6)}
print(f'''
O jogador n° 1 tirou {d["jogador 1"]}
O jogador n° 2 tirou {d["jogador 2"]}
O jogador n° 3 tirou {d["jogador 3"]}
O jogador n° 4 tirou {d["jogador 4"]}
''')
print('Ranking de Jogadores:')
r = sorted(d.items(), key=itemgetter(1), reverse=True)
for c , v in enumerate(r):
    print(f'Em {c+1}° lugar, o {v[0]} com {v[1]} pontos.')
