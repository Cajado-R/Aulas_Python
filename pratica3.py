print('\33[1;31;43mOlá mundo!\033[m')
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
a = 3
b = 5
c = (a + b) * b
print('Os valores são {}  e {} o resultado disso é: {}'.format(cores['azul'], a, cores['limpa'], b, cores['pretoebranco'], c, cores['amarelo']))


