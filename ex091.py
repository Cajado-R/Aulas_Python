from random import randint
from time import sleep

jogadores = []
for i in range(1, 5):
    jogador = dict()
    jogador['Valor'] = randint(1, 6)
    jogador['Nome'] = f'Jogador {i}'
    jogadores.append(jogador)
    sleep(1)
    print(f'{jogador["Nome"]} tirou {jogador["Valor"]}')

print('O ranking foi: ')
ordenado = sorted(jogadores, key=lambda x: x['Valor'], reverse=True)
for i, jogador in enumerate(ordenado):
    sleep(1)
    print(f'{i+1}º Colocado: {jogador["Nome"]}\n '
          f'Com: {jogador["Valor"]}')
