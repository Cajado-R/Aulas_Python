soma = 0
n = 0
for n in range(6):
    n = int(input('digite um número'))
    if n % 2 == 0:
        soma += n
print('O resultado é {}'.format(soma))
