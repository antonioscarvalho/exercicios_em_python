import bisect
l = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    bisect.insort(l, n)
    print(f'Esse número foi indexado na {l.index(n)+1}° posição da lista.')
print(f'A lista seguiu-se da seguinte forma: {l}')