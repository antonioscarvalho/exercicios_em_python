n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
count = 1
while count <= 11:
    if count < 10:
        print(n)
    elif count == 10:
        print(n)
    count = count + 1
    n = n + r

