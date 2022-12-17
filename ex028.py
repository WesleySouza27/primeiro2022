from random import randint
from time import sleep
print('~' * 30)
print('advinhe um numero entre 0 e 5')
print('~' * 30)
num = int(input('digite o seu valor: '))
print('Processando...')
sleep(2) # faz o computador aguardar
aleatorio = randint(0, 5)
if num == aleatorio:
    print('voçê acertou! parabéns')
else:
    print('você perdeu! tente novamente')