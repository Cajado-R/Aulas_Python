quanto = int(input('Que valor quer sacar? R$'))
total = quanto
cedulas = 50
totaldecedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totaldecedulas += 1
    else:
        if totaldecedulas > 0:
            print(f'Total de {totaldecedulas} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totaldecedulas = 0
        if total == 0:
            break

