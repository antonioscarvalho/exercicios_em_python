#Manipulação de texto
nome = str(input('Digite o nome de uma cidade: '))
sep = nome.split()
primnome = sep[0]
tf = 'Santo' in primnome
print('Se "Santo" for o primeiro nome desta cidade, estará escrito: "True"; se não: "False".')
print(tf)