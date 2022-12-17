peso = int(input('qual é o seu peso? kg: '))
altura = float(input('qual é a sua altura? (ex: 1.80): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'seu imc é {imc:.1f} você esta abaixo do peso!')
elif imc > 18.5 and imc < 24.9:
    print(f'seu imc é {imc:.1f} vocé esta no peso ideal!')
elif imc > 25 and imc < 29.9:
    print(f'seu imc é {imc:.1f} você esta acima do peso!')
else:
    print(f'seu imc é {imc} você está obeso(a) cuidado!')
