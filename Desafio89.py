import random
jogos = int(input('Quantos jogos você quer gerar? '))
l = []
c = 0
for c in range(0, jogos):
    for c in range(0, 6):
        n = random.randint(1, 60)
        l.append(n)
    print(l)
    l.clear()