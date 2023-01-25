lista = 'Pão', 1.55, 'Leite', 3.45, 'Ovos', 10.05, 'Macarrão', 13.55
print('*' * 50)

print(f"{'LISTAGEM DE PREÇOS':^50}")

print('*' * 50)
'''
print(lista[0], end='.'*32)
print('R$ ',lista[1])
print(lista[2], end='.'*30)
print('R$ ',lista[3])
print(lista[4], end='.'*31)
print('R$ ',lista[5])
print(lista[6], end='.'*27)
print('R$ ',lista[7])
print('*' * 50)'''
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')