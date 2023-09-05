import random
n = (random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))
print(f'''
A listagem de números gerados aleatóriamente foi: {n};

O menor dos números foi: {min(n)};

O maior dos números foi: {max(n)}.
''')

