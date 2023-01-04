city = input('Digite o nome da cidade: ')
ita = city.upper()
print('Sua cidade se chama {} possui santo no primeiro nome? {}'.format(ita, ita[:5] == 'SANTO'))
