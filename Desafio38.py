n = int(input('Digite um número: '))
print('''Para converter a base do número:
         Digite [1] para base binária.
         Digite [2] para base octal.
         Digite [3] para base hexadecimal.''')
op = int(input('Escolha uma opção: '))
if op == 1:
    print('O número convertido para base binária ficou da seguinte forma: {}'.format(bin(n)[2:]))
elif op == 2:
    print('O número convertido para base octal ficou da seguinte forma: {}'.format(oct(n)[2:]))
elif op == 3:
    print('O número convertido para base hexadecimal ficou da seguinte forma: {}'.format(hex(n)[2:]))
else:
    print('Sua opção deve ser 1, 2 ou 3.')
