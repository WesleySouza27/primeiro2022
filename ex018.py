import math
angulo = float(input('digite o angulo que voçê deseja: '))
seno = math.sin(math.radians(angulo))
consseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f' O seno de {angulo}° é {seno:.2f}\n O cosseno é {consseno:.2f}\n E a tangente é {tangente:.2f}')