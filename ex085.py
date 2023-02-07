lista = [[], []]
numeros = 0

for c in range(1, 8):
    numeros = int(input(f'Digite o {c}º número'))
    if numeros % 2 == 0:
        lista[0].append(numeros)
    if numeros % 2 != 0:
        lista[1].append(numeros)

print(f'Temos os valores: {lista}')

lista[0].sort()
lista[1].sort()

print(f'Os valores pares foram: {lista[0]}')
print(f'Os valores impares foram: {lista[1]}')