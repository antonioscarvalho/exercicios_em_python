def fatorial(a=0):
    f = 1
    for c in range(a, 1, -1):
        f = f * c
    return f
    
numero = int(input('Digite um número para saber seu fatorial: '))
print(f'{numero}! = {fatorial(numero)}')
p = str(input('Quer mostrar o processo do cálculo acima? [S/N] ')).upper().lstrip().rstrip()
for c in range(numero, 0, -1):
    if p == 'S':
        print(c, end='')
        if c > 1:
            print(' x ', end='')
        else:
            print(f' = {fatorial(numero)}')
    else:
        print('---FIM---')