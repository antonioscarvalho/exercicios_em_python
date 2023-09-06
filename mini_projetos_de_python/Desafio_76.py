l = []
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
t = (n1, n2, n3, n4)
print(f' Você digitou: {t}')
q = t.count(9)
print(f'O número 9 apareceu em {q} resposta(s);')
for c in t:
    if c % 2 == 0:
        l.append(c)
print(f'Os números pares digitados: {l};')
if 3 in t:
    p = t.index(3)
    u = p + 1
    print(f'O primeiro 3 aparece na {u}° posição;')
else:
    print('O número 3 não apareceu nenhuma vez entre os digitados.')