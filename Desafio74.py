t = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Internacional', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Fortaleza', 'São Paulo', 'Chapecoense', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Grêmio', 'Vasco', 'Bahia', 'Cuiabá')
p = (t.index('Chapecoense')) + 1
print(f'''
Os 5 primeiros times colocados no Brasileirão 2023:
      
{t[0]};
{t[1]};
{t[2]};
{t[3]};
{t[4]}.

Os 4 últimos colocados da tabela:

{t[16]};
{t[17]};
{t[18]};
{t[19]}.

Lista com os times em ordem alfabética:

{sorted(t)}.

Em qual posição está o time Chapecoense:

Posição n° {p}.
''')