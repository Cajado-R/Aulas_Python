numero = int(input('Digite um número'))
#número de 0 a 9999
uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena {}'.format(cen))
print('Milhar {}'.format(mil))