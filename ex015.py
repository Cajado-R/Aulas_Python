kmrodados = float(input('Digite o número de KM rodados: ' ))
diasalug = float(input('Digite o número de dias utilizado: ' ))
resultado = (diasalug * 60) + (kmrodados * 0.15)
print('Você utilizou o carro por {}KM e ficou com ele por {} dias portanto será necessário pagar {}R$'.format(kmrodados, diasalug, resultado))