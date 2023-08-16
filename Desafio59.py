s = 1
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if s == 'M':
        print('Entendo, seu sexo é {}asculino, então.'.format(s))
    if s == 'F':
        print('Entendo, seu sexo é {}eminino, então.'.format(s))
    elif s != 'M' and s != 'F':
        print('Opção inválida, tente novamente.')
print('FIM')
