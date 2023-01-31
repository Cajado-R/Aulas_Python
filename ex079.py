numeros = list()
while True:
    num = int(input('Digite um número: '))
    if num in numeros:
        print('Este valor já existe')
    else:
        print('Valor adicionado com sucesso')
        numeros.append(num)
    lista = numeros
    continuar = str(input('Deseja Continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print(f'A sua lista recebeu os números: {sorted(lista)}')
