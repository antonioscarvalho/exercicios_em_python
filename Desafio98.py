def area(larg, comp):
    print(f'''
A largura do terreno é: {larg:.1f}. O comprimento do terreno é: {comp:.1f}''')
    area = float(larg * comp)
    print(f'''
A área deste terreno é a largura * comprimento = {area}m²''')
larg = float(input('Qual a largura do terreno? '))
comp = float(input('Qual o comprimento do terreno? '))
area(larg, comp)


