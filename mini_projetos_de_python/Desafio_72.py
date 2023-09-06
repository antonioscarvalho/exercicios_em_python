print('''
O valor a ser sacado deve ser de um número inteiro.
Este programa mostrará a quantidade de cada cédula/moeda que você receberá.
Só serão sacadas as de R$50,00; R$20,00; R$10,00; R$1,00.
          ''')
v = int(input('Qual valor será sacado? '))
f1 = int(v / 50)
v = v - (f1*50)
f2 = int(v / 20)
v = v - (f2*20)
f3 = int(v / 10)
v = v - (f3*10)
f4 = int(v / 1)
print(f'''
      {f1} cédulas de R$50,00;
      {f2} cédulas de R$20,00;
      {f3} cédulas de R$10,00;
      {f4} moeda(s) de R$1,00.''')