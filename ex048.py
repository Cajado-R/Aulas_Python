#vide print de número 1
soma = 0
result = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
print('O resultado da soma de todos os números impares, multiplos de 3 que se encontram no intervalo de 1 a 500 é \033[1;33m{}'.format(soma))
print('FIM')