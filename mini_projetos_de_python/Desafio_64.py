n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
count = 1
while count <= 10:
    if count < 10:
        print(n)
    elif count == 10:
        print(n)
    count = count + 1
    n = n + r
m = 10
m = int(input('Quantos termos a mais você quer: '))
while count <= 11 + m:
    if count < 10 + m:
        print(n)
    elif count == 10 + m:
        print(n)
    count = count + 1
    n = n  + r
    if m == 0:
        break