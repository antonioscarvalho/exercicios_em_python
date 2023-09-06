c = 0
s = 0
n = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c = c + 1
    s = s + n
print('{0} números foram digitados e a soma desses números é {1}.'.format(c, s))