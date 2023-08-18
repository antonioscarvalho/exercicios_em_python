l = []
a = 0
while a != 'N':
    n = int(input('Digite um número: '))
    l.append(n)
    a = str(input('Quer continuar? [S/N] ')).upper().lstrip().rstrip()
print(f'A lista formada ficou da seguinte maneira: {l}')
w = len(l)
print(f'Essa lista tem {w} número(s).')
if 5 in l:
    print(f'O valor 5 foi digitado e encontra-se na {l.index[5]+1}° posição da lista.')
else:
    print('O valor 5 não foi digitado.')
l.sort(reverse=True)
print(f'A lista em contagem decrescente fica da seguinte forma: {l}')
