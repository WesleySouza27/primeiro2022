velocidade = int(input('qual é a velocidade do carro? '))
v = 80
if velocidade > v:
    print(f'voçê ultrapassou o limite de velocidade, o valor da multa ficou em R${(velocidade - v) * 7:.2f}')
print('dirija com cuidado e tenha um bom dia!')