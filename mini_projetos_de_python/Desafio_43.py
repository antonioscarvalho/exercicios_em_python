print('Escreva o comprimento de 3 retas para ver se elas conseguem formar um triângulo:')
a = float(input('Qual o comprimento da reta a? '))
b = float(input('Qual o comprimento da reta b? '))
c = float(input('Qual o comprimento da reta c? '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Elas conseguem formar um triâgulo.')
    if a == b == c:
        print('E esse triângulo é equilatero.')
    elif a == b or a == c or b == c:
        print('E esse triângulo é isóceles.')
    elif a != b != c:
        print('E esse triângulo é escaleno.')
else:
    print('Não conseguem formar um triângulo.')