import random
n = random.randint(1, 6)
adv = int(input('Advinhe o número que foi sorteado do 1 ao 5 pelo computador: '))
if n == adv:
    print('Você acertou!')
else:
    print('Você errou!')    