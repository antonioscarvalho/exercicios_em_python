import random
n = random.randint(0, 11)
c = 0
e = ()
while n != e:
    e = int(input('Advinhe o número que foi sorteado do 0 ao 10 pelo computador: '))
    c = c + 1
    if n == e:
        print('Parabéns, você acertou!')
    else:
        print('Não acertou, chute outro número.')
print('Você chutou {0} vezes.'.format(c))
