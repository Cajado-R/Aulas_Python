import math
angulo = float(input('Digite um ângulo: ' ))
radiano = math.radians(angulo)
print('O ângulo obtido foi: {}, o seno é {:.2f}, coseno {:.2f} e tangente {:.2f}'.format(angulo, math.sin(radiano), math.cos(radiano), math.tan(radiano)))