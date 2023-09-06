vel = int(input('Qual era a velocidade do carro em quilometros? '))
mult = float((vel - 80) * 7.00)
print('Se a velocidade do carro era {0} km/h:'.format(vel))
if vel <= 80:
    print('Tudo bem, você não foi multado, o limite da via era 80km/h.')
else:
    print('Você foi multado, visto que limite da via era 80km/h. A multa será no valor de R${0:.2f}.'.format(mult))