lista = []

while True:

    nome = str(input('nome: '))
    nota1 = float(input('nota 1 '))
    nota2 = float(input('nota 2 '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Desja continuar: [S/N]')).upper().strip()

    if continuar == 'N':
        break

print(lista)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print(30 * '-')

for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:

    print('-' * 30)
    opc = int(input('Notas de quem? [[999] - se quiser interromper]: '))

    if opc == 999:
        print('Finalizando...')
        break

    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
