count1 = 0
count2 = 0
for c in range(1, 8):
    p = int(input('Qual o ano de nascimento dessa pessoa? '))
    m = 2023 - p
    if m > 18:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print('{} dessas pessoas já atingiram a maioridade, já a(s) outra(s) {} não.'.format(count1, count2))