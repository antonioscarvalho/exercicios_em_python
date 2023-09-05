def lin(a):
    x = len(a) + 2
    print('~'*x)
    print(f' {a}')
    print('~'*x)

a = str(input('Digite uma frase para destacá-la com espaços preenchidos por linhas em cima e abaixo: '))
lin(a)