from random import randint
from time import sleep


numeros = []


def sorteia5():
    for n in range(5):
        numeros.append(randint(0,100))
    print('sorteando 5 valores da lista:',end=' ')
    print('[',end='')
    for v in numeros:
        print('',v,end=' ')
        sleep(0.4)
    print('] PRONTO!')




def somapar():
    total = 0
    for v in numeros:
        if v % 2 == 0:
            total += v
    print(f'O maior valor é {total}')
sorteia5()
somapar()