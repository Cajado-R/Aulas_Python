jogador = dict()
time = list()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: \n'))
    numpartidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? \n'))
    partidas.clear()

    for c in range(numpartidas):
        partidas.append(int(input(f'Quantos gols na partida {c + 1} fez? \n')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    continuar = str(input('Deseja continuar: [S/N] \n')).upper()[0]

    if continuar in 'sS':
        continue
    break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-----' * 25)
for i, j in enumerate(time):
    print(f'{i:>3}', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-----' * 25)
while True:
    busca = int(input('Mostrar dados de qual jogador [999/Para]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Error')
    else:
        print(f'Jogador: {time[busca]["nome"]}')
        for i, gol in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {gol} gols.')
    print('-' * 25)