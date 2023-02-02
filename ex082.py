listapares = []
listaimpares = []
lista = []
while True:
    num = int(input('Digite um número: ' ))
    deseja_continuar = str(input('Deseja continuar? [S/N] ' )).upper().strip()
    if deseja_continuar == 'S':
        if num % 2 == 0:
            lista.append(num)
            listapares.append(num)
        if num % 2 != 0:
            lista.append(num)
            listaimpares.append(num)
        continue
    if deseja_continuar == 'N':
        if num % 2 == 0:
            lista.append(num)
            listapares.append(num)
        if num % 2 != 0:
            lista.append(num)
            listaimpares.append(num)
        break
    else:
        print('[ERROR] [S/N] [ERROR]')
        continue
print(f'A lista é: {lista}')
print(f'A lista de números pares é: {listapares}')
print(f'A lista de números impares é: {listaimpares}')
