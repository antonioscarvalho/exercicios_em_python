val = float(input('Qual o valor a ser pago por esse produto? R$'))
print('''Escolha a opção de pagamanto:
      À vista, com 10% de desconto:               Digite [1]
      À vista no cartão, com 5% de desconto:      Digite [2]
      Em até 2x no cartão, a preço normal:        Digite [3]
      3x ou mais, no cartão, com 20% de juros:    Digite [4]''')
opc = int(input('Digite a opção de compra: '))
vist = val-(val*0.10)
cart = val-(val*0.05)
xx = val/2
xxx = val+(val*0.20)
if opc == 1:
    print('O valor a ser pago à vista é: R${0:.2f}.'.format(vist))
elif opc == 2:
    print('O valor a ser pago à vista no cartão é: R${0:.2f}.'.format(cart))
elif opc == 3:
    print('O valor a ser pago em até 2x no cartão é: R${0:.2f} por 2 meses.'.format(xx))
elif opc == 4:
    vzs = int(input('Em quantas vezes (mensalidades) você quer pagar? '))
    xv = xxx/vzs
    print('O valor a ser pago em até 3x no cartão é: R${0:.2f} com mensalidades de {1:.2f} por {2} meses.'.format(xxx, xv, vzs))
else:
    print('Opção inválida. Escolha as opções de 1 a 4.')
    


