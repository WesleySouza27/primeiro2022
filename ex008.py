n1 = int(input('digite a quantidade de metros a ser convertida '))
cm = n1 * 100
mm = n1 * 1000
dc = n1 * 10
dec = n1 / 10
hec = n1 / 100
km = n1 / 1000
print(f'Esta quantidade de metros possui {dc} decimetros {cm} centimetros e {mm} milimetros.')
print(f'{dec} decametros {hec} hectometros e {km} kilômetros.')