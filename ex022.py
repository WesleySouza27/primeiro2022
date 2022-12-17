nome = str(input('nome completo? ')).strip()
print(f'Analisando o seu nome...')
print(f'Seu nome em letras maiusculas {nome.upper()}')
print(f'Seu nome em letras minusculas {nome.lower()}')
so_letras1 = nome.split() #transforma a str em lista[]
so_letras2 = ''.join(so_letras1) #substitui os espaços por "nada"
print(f'Seu nome tem {len(so_letras2)} letras')
a = so_letras1[0]
print(f'Seu primeiro nome é {a} e ele tem {len(a)} letras!')
