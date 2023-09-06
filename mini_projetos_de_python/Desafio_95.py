import time
d = {}
l = []
p = 0   
s = m = c = 0
while p != 'N':
    d.clear()
    d['nome'] = str(input('Qual o nome? ')).capitalize()
    while True: 
        d['idade'] = int(input('Qual a idade? '))
        d['sexo'] = str(input('Qual o sexo? [M/F] ')).upper().rstrip().lstrip()
        if d['sexo'] in 'MF':
            break
    s = s + d['idade']
    c = c + 1
    l.append(d.copy())
    p = str(input('Quer continuar a adicionar pessoas? [S/N] ')).upper().rstrip().lstrip()
media = s / len(l)
a = 0
print(f'''
-------Dados Cadastrados:-------
      
{c} pessoas foram cadastradas.

A média de idade é {media:.1f}.
''')
time.sleep(5)
print(f'Mulheres que foram cadastradas: ', end='')
for d in l:
    if d['sexo'] == 'F':
        a = a + 1 
        print(f'{d["nome"]}. ', end='')
time.sleep(3)
print(f'''
{a} mulheres ao todo.''')
time.sleep(2)
print(f'''
Lista das pessoas que estão acima da média de idade: ''', end='')
for d in l:
    if d['idade'] > media:
        print(' ')
        for h, i in d.items():
            print(f'{h} = {i}; ', end='')
        print()
        time.sleep(5)
print('''
<<<FIM>>>''')
time.sleep(2)