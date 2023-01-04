import math
catetomaior = float(input('Digite o cateto maior do triangulo'))
catetomenor = float(input('Digite o cateto menor do triangulo'))
hipotenuza = math.hypot(catetomaior, catetomenor)
print('A hipotenusa de um triangulo retangulo com medidas {} e {} é igual à {:.2f}'.format(catetomaior, catetomenor, hipotenuza))