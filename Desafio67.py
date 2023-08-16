c = 0
s = 0
l = []
print('''
Este programa terá como saída:
      
    - A média dos números digitados
    - O maior número digitado
    - O menor número digitado
      
Para você parar de digitar números, escreva a palavra "Pare" e nada mais.
      ''')
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Digite "S" para continuar e "N" para parar. [S/N] ')).upper()
    s = s + n
    c = c + 1
    l.append(n)
    x = l[:]
    if r == 'N':
        break
y = max(x)
z = min(x)
m = float(s/c)
print('A média dos números digitados é {0:.1f}, o maior deles é {1} e o menor é {2}.'.format(m, y, z))