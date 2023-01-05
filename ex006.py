from math import sqrt
num = int(input('Digite um número'))
print('\033[3;33;47mO dobro de {} é {}, o triplo é {} e a raiz quadrada é {} \033[m'.format(num, num*2, num*3, sqrt(num)))
