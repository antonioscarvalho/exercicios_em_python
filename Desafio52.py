s = 0
co = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))    
    if n % 2 == 0:
        s = s + n
        co = co + 1
print('A soma dos {0} números pares é {1}.'.format(co, s))
