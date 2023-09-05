#Sorteio
import random
n1 = input('Digite o nome do 1° aluno: ')
n2 = input('Digite o nome do 2° aluno: ')
n3 = input('Digite o nome do 3° aluno: ')
n4 = input('Digite o nome do 4° aluno: ')
lista = [n1, n2, n3, n4]
sort = random.choice(lista)
print('O aluno sorteado foi o(a) {}.'.format(sort))