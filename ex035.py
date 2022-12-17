line1 = float(input('qual o valor da 1° medida? '))
line2 = float(input('qual é o valor da 2° medida? '))
line3 = float(input('qual é o valor da 3° medida? '))

if (line1 + line2 > line3) and (line1 + line3 > line2) and (line2 + line3 > line1):
    print('As medidas informadas são capazes de formar um triângulo!')
else:
    print('as medidas não conseguem formar um triângulo!')
