n = int(input('Quantos termos da sequência de Fibonacci você deseja ver? '))
n1 = 0
n2 = 1
n3 = 1
c = 0
while c <= n-1:
    print(n1, end = ' -> ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    c = c + 1
print('FIM.')
