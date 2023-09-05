def count1(*n1):
    print('A contagem de 1 até 10 de 1 em 1: ')
count1()
for c in range(1, 11):
        print(c, end=' ')
print()


def count2(*n2):
      print('A contagem de 10 até 0 de 2 em 2: ')
count2()
for c in range(10, -1, -2):
        print(c, end=' ')
print()

def count3():
       print('Personalize sua própria contagem: ')
count3()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
pulo = int(input('De quantos em quantos: '))
for c in range(inicio, fim+1, pulo):
        print(c, end=' ')
