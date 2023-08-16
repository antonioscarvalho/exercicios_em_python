n1 = float(input('Qual foi a primeira nota? '))
n2 = float(input('Qual foi a segunda nota? '))
media = float((n1 + n2)/2)
if media < 5:
    print('Reprovado.')
elif 5 <= media <= 6.9:
    print('Recuperação.')
else:
    print('Aprovado.')