from random import randint


lista = list()


def randomizar():
    print(f'Aguarde estou gerando números: ', end=' ')
    for v in range(0, 8):
        va = randint(1, 100)
        lista.append(va)
    print(f'{lista}')


def pares():
    par = 0
    print(f'Somando os valores pares dessa lista: {lista} obtemos como resposta →', end=' ')
    for num in lista:
        if num % 2 == 0:
            par += num
    print(par)


randomizar()
pares()
