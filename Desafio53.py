#Progressão Aritmédica do 1° até o 10° termos
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
dec = n + (10-1) * r #n-ésimo termo
for c in range(n, dec+r, r):
    print(c, end=' ')
