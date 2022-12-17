dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qunatos KM rodados? '))
#diariaD = dias * 60
#diariaK = quantkm * 0.15
#alugel = diariaK + diariaD
pago = (dias * 60) + (km * 0.15)
print(f'O valor do aluguel ficou por R${pago:.2f}')
