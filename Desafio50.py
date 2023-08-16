co = 0 #O contador vai servir para mostrar quantos números 
s = 0 #O somatório vai mostrar a soma de todos os números   
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        co = co + 1
print('A soma de todos os {0} números é {1}.'.format(co, s))