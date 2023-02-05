'''matriz =  [[], [], []]
matriz2 = [[], [], []]
matriz3 = [[], [], []]
numero = int(input(f'Digite o valor na matriz 0, 0'))
matriz[0].append(numero)
numero = int(input(f'Digite o valor na matriz 0, 1'))
matriz[1].append(numero)
numero = int(input(f'Digite o valor na matriz 0, 2'))
matriz[2].append(numero)
numero = int(input(f'Digite o valor na matriz 1, 0'))
matriz2[0].append(numero)
numero = int(input(f'Digite o valor na matriz 1, 1'))
matriz2[1].append(numero)
numero = int(input(f'Digite o valor na matriz 1, 2'))
matriz2[2].append(numero)
numero = int(input(f'Digite o valor na matriz 2, 0'))
matriz3[0].append(numero)
numero = int(input(f'Digite o valor na matriz 2, 1'))
matriz3[1].append(numero)
numero = int(input(f'Digite o valor na matriz 2, 2'))
matriz3[2].append(numero)
print(f'{matriz}\n {matriz2}\n {matriz3}')'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()