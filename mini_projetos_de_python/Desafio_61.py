c = 0
opc = 0
while opc != 1 and opc != 2 and opc != 3:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print('''
Para fazer determinada operação, coloque:
          
    SOMAR:             [1]
    MULTIPLICAR:       [2]
    MAIOR:             [3]
    REPITA O PROGRAMA: [4]
    SAIR DO PROGRAMA:  [5]
          ''')
    opc = int(input('Digite a opção de número escolhida: '))
    if opc == 1:
        s = n1 + n2
        print('A soma dos dois primeiros números digitados é:',s)
        break
    if opc == 2:
        m = n1 * n2
        print('A multiplicação dos dois primeiros números digitados é:',m)
        break
    if opc == 3:
        l = [n1, n2]
        ma = max(l)
        print('Entre os dois números escolhidos, o número {} é o maior.'.format(ma))
        break
    if opc == 4:
        print('Faça tudo de novo.')
        continue
    if opc == 5:
        print('Você escolheu parar o programa.')
        break
