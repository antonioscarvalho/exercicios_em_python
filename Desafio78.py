t = ('Fruta', 'Automoveis', 'Bebidas', 'Elementos', 'Tarefas')
for c in t:
    print(f'\nNa palavra "{c.capitalize()}" há as vogais: ',end = '')
    for v in c:
        if v.lower() in 'aeiou':    
            print(v.lower(), end = ' ')