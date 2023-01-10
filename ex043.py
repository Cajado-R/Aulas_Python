"""IMC CALCULO"""
print(50*'-')
print('CALCULADORA DE IMC')
print(50*'-')
peso = float(input('Digite seu peso'))
alt = float(input('Digite a sua altura em metros'))
IMC = peso / (alt*alt)
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC < 24.9:
    print('Peso ideal')
elif IMC < 29:
    print('Pré-Obesidade')
elif IMC < 35:
    print('Obeso')
elif IMC < 39:
    print('Obesidade grau 2')
elif IMC > 40:
    print('Obesidade morbida')
else:
    print('Há algo errado')