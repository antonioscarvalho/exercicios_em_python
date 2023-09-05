print('Escreva o comprimento de 3 retas para ver se elas conseguem formar um triângulo:')
a = float(input('Qual o comprimento da reta a? '))
b = float(input('Qual o comprimento da reta b? '))
c = float(input('Qual o comprimento da reta c? '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Elas conseguem formar um triâgulo.')
else:
    print('Não conseguem formar um triângulo.')