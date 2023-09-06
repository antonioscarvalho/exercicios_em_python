l = [[], [], []]
for c in range(0, 3):
    for c in range(0, 3):
        n = int(input('Digite um número: '))
        l[c].append(n)
print(f'''
    |{l[0][0]}| |{l[0][1]}| |{l[0][2]}|
    |{l[1][0]}| |{l[1][1]}| |{l[1][2]}|
    |{l[2][0]}| |{l[2][1]}| |{l[2][2]}|
''')