nome = str(input('Qual é o seu nome completo? ')).strip()
div = nome.lower().split()
s = 'silva' in div
print(f'Seu nome tem silva? {s}')
