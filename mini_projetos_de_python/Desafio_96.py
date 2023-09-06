p = 0
l1 = []
while p != 'N':
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
    l1.append(d.copy())
    print(f'''
    {d}
    ''')

    for c, v in d.items():
        print(f'O campo {c} foi preenchido com {v}.')

    print(f'''
O jogador {d["nome"]} jogou {part} partidas:''')
    for c in range(0, part):
        print(f'-> Na {c+1}° partida fez {l[c]} gols.')
    print(f'''
Ou seja, foi um total de {d["total"]} gols.
''')
    p = str(input('Quer continuar a adicionar jogadores? [S/N] ')).upper().rstrip().lstrip()
p1 = 0
while p1 != 999:
    p1 = int(input('Quer ver dados de algum jogador? Qual? (0, para o primeiro jogador digitado, 1 para o segundo, etc.)'))
    if p1 >= len(l1):
        print(f'Não há jogadores com este código de busca.')
    else:
        print('''
Levantamento do rendimento:
              ''')
        for b, e in enumerate((l1[p1]['gols'])):
            print(f'''No {b+1}° jogo, fez {e} gols.''')
print('''
Análise de aproveitamento concluída.''')