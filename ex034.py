salario = float(input('qual é o seu salário? '))
if salario > 1250.00:
    print(f'esse é o seu novo salario com 10% de aumento! R${salario + (salario * 10 / 100):.2f}')
else:
    print(f'esse é o seu novo salario com 15% de aumento! R${salario + (salario * 15 / 100):.2f}')
