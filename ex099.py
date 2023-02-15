from time import sleep


def valores(* num):
    print('Analisando os valores vejo que temos: ', end=' ')
    tamanho = maior = 0
    for v in num:
        maior == v
        if v > maior:
            maior = v
        tamanho += 1
    print(f'{num}', f'Foram informados {tamanho} números ao todo')
    print(f'O maior número foi {maior}')


valores(1, 2, 3, 4, 6, 8)
valores(8, 45, 32, 56, 10)