from math import hypot
C_oposto = float(input('digite o comprimento do cateto oposto: '))
C_adjacente = float(input('digite o comprimeto do cateto adjacente: '))
#A hipotenusa é a raiz quadrada da soma dos quadrados dos catetes
#hipotenusa = (C_oposto ** 2 + C_adjacente ** 2) ** (1/2)
hipotenusa = hypot(C_oposto, C_adjacente)
print(f'a hupotenusa equivale a {hipotenusa:.2f}')
