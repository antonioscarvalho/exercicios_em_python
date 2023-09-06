l = []
def maior():
    p = 0
    while p != 'N':
        n = int(input('Digite um número: '))
        p = str(input('Quer continuar? [S/N] ')).lstrip().rstrip().upper()
        l.append(n)

maior()
print(f'A lista com os números digitados ficou da seguinte forma: {l}')
print(f'O total de números na lista é: {len(l)}')
x = max(l)
print(f'O maior número da lista é: {x}')