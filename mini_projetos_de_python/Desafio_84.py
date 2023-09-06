e = str(input('Digite sua expressão: '))
l = []
for p in e:
    if p == '(':
        l.append('(')
    elif p == ')':
        if len(l) > 0:
            l.pop()
        else:
           l.append(')')
           break
if len(l) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')