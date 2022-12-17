distancia = float(input('qual é a distancia em KM da sua viagem? '))
if distancia > 200:
    print(f'o valor da sua passagem ficou por: R${distancia * 0.45:.2f}')
else:
    print(f'o valor da sua passagem ficou por: R${distancia * 0.5:.2f}')
