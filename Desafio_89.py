import random
jogos = int(input('Quantos jogos você quer gerar? '))
l = []
c = 0
for c in range(0, jogos):
    for count in range(0, 6):
        n = random.sample(range(1, 60), 1)
        l.append(n)
    c = c + 1
    print(f'{c}° opção de jogo: {l}')
    l.clear()