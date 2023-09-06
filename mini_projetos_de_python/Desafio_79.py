n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
n5 = int(input('Digite outro número: '))
l = [n1, n2, n3, n4, n5]
x = min(l)
y = max(l)
p1 = l.index(x)
p2 = l.index(y)
print(f'''
Os números digitados foram: {l}.
O menor número está na {p1+1}° posição, é o {x}. 
O maior que está na {p2+1}° posição, é o {y}.
''')