triangulo1 = float(input('Digite o primeiro angulo'))
triangulo2 = float(input('Digite o segundo angulo'))
triangulo3 = float(input('Digite o terceiro angulo'))
if triangulo1 < triangulo2 + triangulo3 and triangulo2 < triangulo1 + triangulo3 and triangulo3 < triangulo1 + triangulo2:
    print('Ele pode ser um triangulo')
else:
    print('Infelizmente isso não pode ser um triangulo')