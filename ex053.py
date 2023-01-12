frase = str(input('Digite para saber se é um palindromo')).replace(' ', '')
frasal = frase[::-1]
if frase == frasal:
    print('A FRASE {} -- {} É UM PALINDROMO'.format(frase, frasal))
else:
    print('A FRASE {} -- {} NÃO É UM PALINDROMO'.format(frase, frasal))
