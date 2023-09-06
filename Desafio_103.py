def voto():
    ano = int(input('Qual o ano de nascimento da pessoa? '))
    n = 2023 - ano
    if n >= 18 and n <= 59:
        print(f'Com {n} anos, seu voto é obrigatório.')
    elif n == 16 or n == 17 or n >= 60:
        print(f'Com {n} anos, seu voto é facultativo.')
    else:
        print(f'Com {n} anos, você não pode votar.')

voto()