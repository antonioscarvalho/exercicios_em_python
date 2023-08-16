l = []
c = 1
co = 0
co2 = 0
so = 0
idoso = 0
nidoso = []
while c > 0:
    c += 1
    x = c - 1
    print('{}° pessoa: '.format(x))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    l.append(idade)
    x = l[1:5]
    sexo = str(input('Sexo [M/F]: ')).upper()
    q = str(input('Quer continuar a adcionar pessoas? [S/N] ')).upper().lstrip().rstrip()
    if q == 'N':
        break
    if idade == idade:
        so = so + idade
        co = co + 1
    if (sexo == 'F') and idade < 20:
        co2 = co2 + 1
    if c == 1 and sexo == 'M':
        idoso = idade
        nidoso = nome
    if sexo =='M' and idoso < idade:
        idoso = idade
        nidoso = nome
medidade = so / co
print('''Algumas considerações: 
            A média de idade do grupo é: {0}.
            O nome do homem mais velho é: {2}.
            A quantidade de mulheres com menos de 20 anos é: {1}.'''.format(medidade, co2, nidoso))
