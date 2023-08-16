import random
print('Jokenpô com o computador.')
print('''
      Para escolher pedra:   Digite [1]
      Para escolher papel:   Digite [2]
      Para escolher tesoura: Digite [3]
      ''')
esc = int(input('Escolha a opção que deseja. '))
seq = [1, 2, 3]
comp = random.choice(seq)
if esc == 1 and comp == 1:
    print('Empate, visto que você e o computador escolheram pedra.')
elif esc == 1 and comp == 2:
    print('O computador escolheu papel e você pedra, logo ele ganhou de você.')
elif esc == 1 and comp == 3:
    print('O computador escolheu tesoura e você pedra, logo você ganhou!')
elif esc == 2 and comp == 2:
    print('Empate, visto que você e o computador escolheram papel.')
elif esc == 2 and comp == 1:
    print('O computador escolheu pedra e você papel, logo você ganhou!')
elif esc == 2 and comp == 3:
    print('O computador escolheu tesoura e você papel, logo ele ganhou de você.')
elif esc == 3 and comp == 3:
    print('Empate, visto que você e o computador escolheram tesoura.')
elif esc == 3 and comp == 1:
    print('O computador escolheu pedra e você tesoura, logo ele ganhou de você.')
elif esc == 3 and comp == 2:
    print('O computador escolheu papel e você tesoura, logo você ganhou!')
else:
    print('Opção inválida. Você deve escrever um número de 1 a 3 para jogar.')
