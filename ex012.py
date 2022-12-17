preço = float(input('qual é o valor do produto? R$ '))
#d = preço * 0.95
d = preço - (preço * 5 / 100)
print(f'com 5% de desconto,o produto fica no valor de R${d:.2f} ')
