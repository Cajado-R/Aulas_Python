matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
coluna = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
for l in range(0, 3):
    coluna += matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'A soma dos pares é: {pares}')
print(f'A soma da coluna 3 é: {coluna}')
print(f'O maior valor da coluna 2 é: {maior}')