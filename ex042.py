triangulo1 = float(input('Digite o primeiro angulo'))
triangulo2 = float(input('Digite o segundo angulo'))
triangulo3 = float(input('Digite o terceiro angulo'))
if triangulo1 < triangulo2 + triangulo3 and triangulo2 < triangulo1 + triangulo3 and triangulo3 < triangulo1 + triangulo2:
    if triangulo1 != triangulo2 and triangulo3 != triangulo1 and triangulo2 != triangulo3:
        print('ESCALENO')
    elif triangulo1 == triangulo2 and triangulo3 == triangulo1:
        print('EQUILÁTERO')
    elif triangulo1 == triangulo2 or triangulo3 == triangulo1 or triangulo2 == triangulo3:
        print('ISÓCELES')
else:
    print('Não é possível fazer um trinagulo com essas retas')