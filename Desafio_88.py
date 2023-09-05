s = 0
l = [[], [], []]
for c in range(0, 3):
    for c in range(0, 3):
        n = int(input('Digite um número: '))
        l[c].append(n)
        s = s + n
x = max(l[1])
print(f'''
    |{l[0][0]}| |{l[0][1]}| |{l[0][2]}|
    |{l[1][0]}| |{l[1][1]}| |{l[1][2]}|
    |{l[2][0]}| |{l[2][1]}| |{l[2][2]}|
    ''')
print(f'Todos os valores digitados e colocados na matriz acima somados dão: {s}')
print(f'Os valores da terceira coluna somados dão: {l[0][2]+l[1][2]+l[2][2]}')
print(f'O maior valor da segunda linha é: {x}')