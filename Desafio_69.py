import random
chute = ['PAR', 'IMPAR']
p = 'PAR'
i = 'IMPAR'
c = 0
while True:
    ch = str(input('Digite "par" ou "impar" para jogar com o computador: ')).upper().rstrip().lstrip()
    s = random.choice(chute)
    c = c + 1
    x = c - 1
    if ch == s:
        print('Parabéns, você ganhou, jogue mais uma rodada!')
    else:
        break
print(f'Você perdeu, seu número de vitórias foi {x}.')
    
    